# Generated by Django 5.0.3 on 2024-03-15 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flashcard',
            name='name',
        ),
    ]
