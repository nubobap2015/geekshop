from django.conf import settings
from django.db import models

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='Время добавления', auto_now_add=True)

    @property
    def _product_cost(self):
        return self.quantity * self.product.price

    @property
    def products(self):
        return Basket.objects.filter(user=self.user)

    @property
    def products_list(self):
        return list(self.products())

    @property
    def total_cost(self):
        _tmp = sum(list(map(lambda x: x._product_cost, self.products)))
        return _tmp if _tmp is not None else 0

    @property
    def total_quantity(self):
        _tmp = sum(list(map(lambda _prod: _prod.quantity, self.products)))
        return _tmp if _tmp is not None else 0

    def _get_product(self, prod_pk):
        my_products = self.products.filter(pk=prod_pk)
        return None if not my_products else my_products[0]

    def add_product(self, prod_pk):
        my_product = self._get_product(prod_pk)
        if my_product is None:
            _tmp_product = Product.objects.filter(pk=prod_pk)
            if not _tmp_product:
                return False
            my_product = Basket(user=self.user, product=_tmp_product[0])
        my_product.quantity += 1
        my_product.save()
        return my_product

    def remove_product(self, prod_pk):
        my_product = self._get_product(prod_pk)
        if my_product is not None:
            my_product.delete()
            return True
        return False

    def set_quantity_of_product(self, prod_pk, count):
        my_product = self._get_product(prod_pk)
        if my_product is None:
            my_product = self.add_product(prod_pk)
        if not my_product:
            return False
        my_product.quantity = count
        return my_product
