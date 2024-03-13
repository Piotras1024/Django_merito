from django.contrib import admin
from django.urls import path
from .views import home, testing, flashcards_list, learn_flashcard

urlpatterns = [
    path('', home, name='home'),
    path('test', testing, name='test'),
    path('list', flashcards_list, name='flash'),
    path('learn/<slug:slug_name>', learn_flashcard, name='learn')
    ]
