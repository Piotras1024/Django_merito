from django.db import models
from django.utils.text import slugify

# Tutaj definiujemy tylko typy
'''

W Django, każdy model automatycznie otrzymuje pole id, 
które służy jako klucz główny (PrimaryKey), jeśli nie 
zdefiniujesz własnego. To pole id jest autoinkrementowane 
i unikalne dla każdego rekordu, co oznacza, że nie musisz 
jawnie dodawać pola id do swojego modelu Flashcard – Django 
robi to za Ciebie w tle.
'''


class Flashcard(models.Model):
    name = models.CharField(max_length=100)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name
