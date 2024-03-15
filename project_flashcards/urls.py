from django.contrib import admin
from django.urls import path, include
from flashcards.views import home


urlpatterns = [
    path('flashcards/', include('flashcards.urls')),
    path('user/', include('user_identification.urls')),
    path('', home),
    path('admin/', admin.site.urls)
]
