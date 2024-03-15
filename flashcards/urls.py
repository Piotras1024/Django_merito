from django.contrib import admin
from django.urls import path
from .views import home, testing, flashcards_list, learn_flashcard, create_deck, deck_flashcards

urlpatterns = [
    path('', home, name='home'),
    path('test', testing, name='test'),
    path('list', flashcards_list, name='flash'),
    path('learn/<slug:slug_name>', learn_flashcard, name='learn'),
    path('create_deck', create_deck, name='create_deck'),
    path('deck/<slug:slug>/', deck_flashcards, name='deck_flashcards'),
    ]
