from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm


def signup_view(request):
    # Logika rejestracji dla niezalogowanych użytkowników
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Zmień 'home' na nazwę URL-a strony głównej
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    # Jeśli 'next' w URL, dodaj komunikat
    if 'next' in request.GET:
        messages.info(request, 'Zaloguj się, zanim stworzysz nowy Deck')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Przekieruj do strony głównej po pomyślnym zalogowaniu
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})