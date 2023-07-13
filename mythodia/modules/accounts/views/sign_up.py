from django.contrib.auth import authenticate, login
from django.views.generic import CreateView

from ..forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "accounts/sign_up.html"
    success_url = "/"

    def form_valid(self, form):
        res = super().form_valid(form)
        login(self.request, self.object)
        return res
