from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=150, error_messages={
        'required': _("Wymagane jest 150 lub mniej znaków. Jedynie litery, cyfry i @/./+/-/_."),
    })

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

'''
Twoje hasło nie może być zbyt podobne do twoich innych danych osobistych.
Twoje hasło musi zawierać co najmniej 8 znaków.
Twoje hasło nie może być powszechnie używanym hasłem.
Twoje hasło nie może składać się tylko z cyfr.


Wprowadź to samo hasło ponownie, dla weryfikacji.
'''
