from django.shortcuts import render, get_object_or_404, redirect
from flashcards.models import Flashcard
from django.contrib.auth.decorators import login_required
from .forms import DeckForm, FlashcardForm
from .models import Deck, Flashcard
from django.utils.text import slugify


def home(request):
    return render(request, 'hello.html')


def flashcards_list(request):
    flashcards: list[Flashcard] = Flashcard.objects.all()
    return render(request, 'flashcards_list.html',
                  context={"flashcards": flashcards})


def testing(request):
    return render(request, 'base.html')


def learn_flashcard(request, slug_name):
    # Pobierz aktualną fiszkę na podstawie slug
    current_flashcard = get_object_or_404(Flashcard, slug=slug_name)

    # Pobierz ID aktualnej fiszki i spróbuj znaleźć następną
    next_flashcard = Flashcard.objects.filter(id__gt=current_flashcard.id).order_by('id').first()

    # Pobierz ID aktualnej fiszki i spróbuj znaleźć poprzednią
    previous_flashcard = Flashcard.objects.filter(id__lt=current_flashcard.id).order_by('-id').first()

    # Jeśli nie ma next_flashcard, przypisz pierwszą fiszkę jako next
    if not next_flashcard:
        next_flashcard = Flashcard.objects.order_by('id').first()

    # Jeśli nie ma previous_flashcard, przypisz ostatnią fiszkę jako previous
    if not previous_flashcard:
        previous_flashcard = Flashcard.objects.order_by('-id').first()

    context = {
        "flashcard": current_flashcard,
        "next_flashcard": next_flashcard,
        "previous_flashcard": previous_flashcard,
    }

    return render(request,
                  'learn_flashcard.html',
                  context=context)


@login_required
def create_deck(request):
    decks = Deck.objects.filter(owner=request.user)
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.owner = request.user
            deck.save()
            return redirect('test')  # zmień na właściwą nazwę widoku
    else:
        form = DeckForm()
    return render(request, 'create_deck.html', {'form': form, "decks": decks})


@login_required
def deck_flashcards(request, slug):
    deck = get_object_or_404(Deck, slug=slug, owner=request.user)
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.deck = deck
            flashcard.save()
            return redirect('deck_flashcards', slug=deck.slug)
    else:
        form = FlashcardForm()
    flashcards = deck.flashcards.all()
    return render(request, 'deck_flashcards.html', {'deck': deck, 'flashcards': flashcards, 'form': form})

# Create your views here.
