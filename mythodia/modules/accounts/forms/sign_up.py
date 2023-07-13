from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

from ..models import Account


class SignUpForm(UserCreationForm):
    TAILWIND_CLASSES = "w-full px-4 py-2 transition duration-300 border border-gray-300 rounded focus:border-transparent focus:outline-none focus:ring-4 focus:ring-blue-200"

    email = forms.EmailField(
        label=_("Email"),
        widget=forms.EmailInput(
            attrs={
                "autofocus": True,
                "class": TAILWIND_CLASSES,
            }
        ),
        help_text=_(""),
    )
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": TAILWIND_CLASSES,
            }
        ),
        help_text=_(""),
    )
    password2 = forms.CharField(
        label=_("Confirm Password"),
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                "class": TAILWIND_CLASSES,
            }
        ),
        help_text=_(""),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Account
        fields = ("email", "password1", "password2")
