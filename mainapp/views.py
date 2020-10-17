import datetime

from django.conf import settings
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import Product, ProductsCategory, Contact


# Create your views here.

def main(request):
    title = "Главная"
    my_products = Product.objects.all()[0:4]
    content = {"myTitle": title, "products": my_products, "media_url": settings.MEDIA_URL,}
    return render(request, "mainapp/index.html", content)


def products(request, pk=None):
    title = "Продукты"
    links_menu = ProductsCategory.objects.all()
    if pk is not None:
        print(f"User select category: {pk}")
        if pk == 0:
            myProducts = Product.objects.all().order_by("price")
            myCatecory = {'name': 'Все'}
        else:
            myCatecory = get_object_or_404(ProductsCategory, pk=pk)
            myProducts = Product.objects.filter(id_cat__pk=pk).order_by("price")
        content = {"myTitle": title,
                   "links_menu": links_menu,
                   "category": myCatecory,
                   "products": myProducts,
                   "media_url": settings.MEDIA_URL,
                   }
        return render(request, "mainapp/products_list.html", content)
    same_products = Product.objects.all()
    content = {"myTitle": title,
               "links_menu": links_menu,
               "same_product": same_products,
               "media_url": settings.MEDIA_URL,
               }
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    visit_date = datetime.datetime.now()
    locations = Contact.objects.all()
    content = {"myTitle": title, "visit_date": visit_date, "locations": locations, "media_url": settings.MEDIA_URL,
               }
    return render(request, "mainapp/contact.html", content)
