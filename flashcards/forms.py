from django import forms
from .models import Deck, Flashcard


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['name']
        # Nie potrzebujesz `slug` w formularzu, może być generowany automatycznie


class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['question', 'answer']
        # `deck` jest potrzebny, aby wskazać, do którego decku fiszka należy
