from django.urls import path, re_path

from .views import *


app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="sign_up"),
]
