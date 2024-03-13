import django.utils.text
from django.shortcuts import render, get_object_or_404
from .models import Flashcard
from flashcards.models import Flashcard
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



# Create your views here.
