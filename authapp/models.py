from django.contrib.auth.models import AbstractUser
from django.db import models

from basketapp.models import Basket


class MyBasket:
    def __init__(self, shop_user):
        MyBasket.shop_user = shop_user


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.IntegerField(verbose_name='Возраст', blank=True, null=True)

    def __init__(self):
        my_Basket = MyBasket(self)

    @property
    def user_basket(self):
        _tmp_baskets = Basket.objects.filter(user=self)
        return None if len(_tmp_baskets) == 0 else _tmp_baskets[0]
