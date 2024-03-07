from django.contrib import admin
from django.urls import path, include
from flashcards.views import home


urlpatterns = [
    path('', include('flashcards.urls')),
    path('', home),
    path('admin/', admin.site.urls)
]
