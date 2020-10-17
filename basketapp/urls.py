from django.urls import path

import basketapp.views as basketapp
from .apps import BasketappConfig

app_name = BasketappConfig.name

urlpatterns = [
    path("", basketapp.basket, name="view"),
    path("add/<int:pk>/", basketapp.basket_add, name="add"),
    path("remove/<int:pk>/", basketapp.basket_remove, name="remove"),
]
