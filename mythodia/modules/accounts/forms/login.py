from django.contrib.auth.forms import (
    UsernameField,
    AuthenticationForm as DjangoAuthenticationForm,
)
from django import forms
from django.utils.translation import gettext_lazy as _


class LoginForm(DjangoAuthenticationForm):
    username = UsernameField(
        label=_("Username"), widget=forms.TextInput(attrs={"autofocus": True})
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
