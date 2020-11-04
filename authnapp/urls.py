from django.urls import re_path

import authnapp.views as authnapp

app_name = "authnapp"

urlpatterns = [
    re_path(r"^login/$", authnapp.login, name="login"),
    re_path(r"^logout/$", authnapp.logout, name="logout"),
    re_path(r"^register/$", authnapp.register, name="register"),
    re_path(r"^edit/$", authnapp.edit, name="edit"),
]
