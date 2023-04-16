from django.urls import path, re_path

from .views import *


app_name = "accounts"

urlpatterns = [path("", LoginView.as_view(), name="login")]
