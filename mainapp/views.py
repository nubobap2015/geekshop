import datetime
from django.conf import settings
from django.shortcuts import render
from .models import Product, ProductsCategory, Contact


# Create your views here.

def main(request):
    title = "Главная"
    my_products = Product.objects.all()[0:4]
    content = {"myTitle": title, "products": my_products, "media_url": settings.MEDIA_URL}
    return render(request, "mainapp/index.html", content)


def products(request, pk=None):
    title = "Продукты"
    links_menu = ProductsCategory.objects.all()
    same_products = Product.objects.all()
    content = {"myTitle": title, "links_menu": links_menu, "same_products":same_products, "media_url": settings.MEDIA_URL}
    if pk:
        print(f"User select category: {pk}")
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    visit_date = datetime.datetime.now()
    locations = Contact.objects.all()
    content = {"myTitle": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contact.html", content)
