import datetime

from django.conf import settings
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import Product, ProductsCategory, Contact


# Create your views here.

def main(request):
    title = "Главная"
    basket = []
    mySum = 0
    my_products = Product.objects.all()[0:4]
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        for basketitems in basket.all():
            mySum += basketitems.quantity * basketitems.product.price

    content = {"myTitle": title, "products": my_products, "media_url": settings.MEDIA_URL, "basket": basket,
               "basketSUMM": mySum, }
    return render(request, "mainapp/index.html", content)


def products(request, pk=None):
    title = "Продукты"
    basket = []
    mySum = 0
    links_menu = ProductsCategory.objects.all()
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        for basketitems in basket.all():
            mySum += basketitems.quantity * basketitems.product.price

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
                   "basket": basket,
                   "basketSUMM": mySum,
                   }
        return render(request, "mainapp/products_list.html", content)
    print('опа')
    same_products = Product.objects.all()
    content = {"myTitle": title,
               "links_menu": links_menu,
               "same_product": same_products,
               "media_url": settings.MEDIA_URL,
               "basket": basket,
               "basketSUMM": mySum,
               }
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    basket = []
    mySum = 0
    visit_date = datetime.datetime.now()
    locations = Contact.objects.all()
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        for basketitems in basket.all():
            mySum += basketitems.quantity * basketitems.product.price
    content = {"myTitle": title, "visit_date": visit_date, "locations": locations, "media_url": settings.MEDIA_URL,
               "basket": basket,
               "basketSUMM": mySum, }
    return render(request, "mainapp/contact.html", content)
