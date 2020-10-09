from django.db import models

# Create your models here.

class ProductCategories(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=255, blank=False)
    desc = models.CharField(verbose_name='Описание', max_length=8000, blank=True)
    #  Служебные
    isDeleted = models.BooleanField(verbose_name='Удалено', default=False)
    date_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_upd = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    id_cat = models.ForeignKey(ProductCategories, on_delete=models.PROTECT)
    name = models.CharField(verbose_name="Наименование", max_length=255, blank=False)
    desc = models.CharField(verbose_name='Описание', max_length=8000, blank=True)
    img_src = models.ImageField(upload_to='products_images', blank=True)
    img_href = models.CharField(verbose_name="Наименование", max_length=255, blank=False)
    price = models.DecimalField(verbose_name='Цена', max_digits=12, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='Кол-во на складе', default=0)
    #  Служебные
    isDeleted = models.BooleanField(verbose_name='Удалено', default=False)
    date_create = models.DateTimeField(verbose_name='Дата создания' ,auto_now_add=True)
    date_upd = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.name.join}[{self.id_cat.name}]{"(удалено)" if self.isDeleted else ""}'

