from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Deck(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='decks')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:  # Jeśli slug nie jest już ustawiony
            self.slug = slugify(self.name)  # Generuj slug z name
        super().save(*args, **kwargs)  # Wywołaj oryginalną metodę save

    def __str__(self):
        return self.name


class Flashcard(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    slug = models.SlugField(max_length=200)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='flashcards')

    def save(self, *args, **kwargs):
        if not self.slug:  # Jeśli slug nie jest już ustawiony
            self.slug = slugify(self.question)  # Generuj slug z name
        super().save(*args, **kwargs)  # Wywołaj oryginalną metodę save

    def __str__(self):
        return self.question

# Tutaj definiujemy tylko typy
'''

W Django, każdy model automatycznie otrzymuje pole id, 
które służy jako klucz główny (PrimaryKey), jeśli nie 
zdefiniujesz własnego. To pole id jest autoinkrementowane 
i unikalne dla każdego rekordu, co oznacza, że nie musisz 
jawnie dodawać pola id do swojego modelu Flashcard – Django 
robi to za Ciebie w tle.
'''
