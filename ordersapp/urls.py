from django.urls import re_path

import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    re_path(r"^$", ordersapp.list, name="list"),
]
