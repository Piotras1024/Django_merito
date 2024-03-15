from django.contrib import admin
from .models import Flashcard


@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    ...

# "slug" -> czyli pole slug wziął dane z name.
