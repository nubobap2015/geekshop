from django.db import models

# Create your models here.

class ProductsCategory(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=255, blank=False)
    href = models.CharField(verbose_name='Ссылка', max_length=255, blank=True)
    desc = models.CharField(verbose_name='Описание', max_length=8000, blank=True)
    #  Служебные
    isDeleted = models.BooleanField(verbose_name='Удалено', default=False)
    date_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_upd = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.name}{"(удалено)" if self.isDeleted else ""}'

class Product(models.Model):
    id_cat = models.ForeignKey(ProductsCategory, on_delete=models.PROTECT)
    name = models.CharField(verbose_name="Наименование", max_length=255, blank=False)
    desc = models.CharField(verbose_name='Описание', max_length=8000, blank=True)
    image_src = models.ImageField(upload_to='products_images', blank=True)
    image_href = models.CharField(verbose_name="Ссылка", max_length=255, blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=12, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='Кол-во на складе', default=0)
    alt = models.CharField(verbose_name='Текст картинки', max_length=8000, blank=True)
    #  Служебные
    isDeleted = models.BooleanField(verbose_name='Удалено', default=False)
    date_create = models.DateTimeField(verbose_name='Дата создания' ,auto_now_add=True)
    date_upd = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.name} [{self.id_cat.name}]{"(удалено)" if self.isDeleted else ""}'

class Contact(models.Model):
    city = models.CharField(verbose_name="Город", max_length=255, blank=False)
    phone = models.CharField(verbose_name="Контактный телефон", max_length=255, blank=False)
    email = models.EmailField(verbose_name="Email", max_length = 255, blank=False)
    address = models.TextField(verbose_name="Адрес", max_length=2000, blank=False)
    #  Служебные
    isDeleted = models.BooleanField(verbose_name='Удалено', default=False)
    date_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_upd = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.city}({self.id})'