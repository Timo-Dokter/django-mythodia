from django.template import Library
from django.contrib.auth.views import LoginView as DjangoLoginView

from ..forms import LoginForm


class LoginView(DjangoLoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"

    register = Library()
