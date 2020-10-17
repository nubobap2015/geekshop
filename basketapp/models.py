from django.conf import settings
from django.db import models

from mainapp.models import Product


# Create your models here.
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
        return list(Basket.objects.filter(user=self.user))

    @property
    def total_cost(self):
        return sum(list(map(lambda x: x._product_cost, self.products)))

    @property
    def total_quantity(self):
        return sum(list(map(lambda _prod: _prod.quantity, self.products)))
