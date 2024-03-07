from django.shortcuts import render
from .models import Flashcard
from flashcards.models import Flashcard


def home(request):
    return render(request, 'hello.html')


def flashcards_list(request):
    flashcards: list[Flashcard] = Flashcard.objects.all()
    return render(request, 'flashcards_list.html',
                  context={"flashcards": flashcards})


def testing(request):
    return render(request, 'base.html')


# Create your views here.
