from django.urls import path, re_path

from .views import *


app_name = "core"

urlpatterns = [path("", Home.as_view(), name="home")]
