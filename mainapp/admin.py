from django.contrib import admin
from .models import ProductsCategory, Product, Contact

# Register your models here.
admin.site.register(ProductsCategory)
admin.site.register(Product)
admin.site.register(Contact)
