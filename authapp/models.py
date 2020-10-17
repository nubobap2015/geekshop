from django.contrib.auth.models import AbstractUser
from django.db import models

from basketapp.models import Basket
from mainapp.models import Product


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.IntegerField(verbose_name='Возраст', blank=True, null=True)

    @property
    def products(self):
        return Basket.objects.filter(user=self)

    @property
    def products_list(self):
        return list(self.products())

    @property
    def total_cost(self):
        _tmp = sum(list(map(lambda x: x.product.price * x.quantity, self.products)))
        return _tmp if _tmp is not None else 0

    @property
    def total_quantity(self):
        _tmp = sum(list(map(lambda _prod: _prod.quantity, self.products)))
        return _tmp if _tmp is not None else 0

    def _get_product(self, prod_pk):
        my_products = self.products.filter(product_id=prod_pk)
        return None if not my_products else my_products[0]

    def _get_basket_product(self, prod_pk):
        my_products = self.products.filter(id=prod_pk)
        return None if not my_products else my_products[0]

    def add_product(self, prod_pk):
        my_product = self._get_product(prod_pk)
        if my_product is None:
            _tmp_product = Product.objects.filter(pk=prod_pk)
            if not _tmp_product:
                return False
            my_product = Basket(user=self, product=_tmp_product[0])
        my_product.quantity += 1
        my_product.save()
        return my_product

    def remove_product(self, prod_pk):
        my_product = self._get_basket_product(prod_pk)
        if my_product is not None:
            my_product.delete()
            return True
        return False

    def set_quantity_of_product(self, prod_pk, count):
        my_product = self._get_basket_product(prod_pk)
        if my_product is None:
            my_product = self.add_product(prod_pk)
        if not my_product:
            return False
        my_product.quantity = count
        return my_product
