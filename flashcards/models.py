from django.db import models


class Flashcard(models.Model):
    name = models.CharField(max_length=100)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return self.name
