import datetime
from django.shortcuts import render


# Create your views here.

def main(request):
    title = "Главная"
    products = [
        {
            'name': 'Отличный стул',
            'desc': 'Расположи седалище комфортно',
            'image_src': 'product-1.jpg',
            'image_href': '/product/1', #Почему "/product/1", а не "/products/1"?
            'alt': 'продукт №1',
        },
        {
            'name': 'Стул повышенного качества',
            'desc': 'НЕ ОТОРВАТЬСЯ',
            'image_src': 'img/product-1.jpg',
            'image_href': '/product/1',
            'alt': '',
        },
    ]
    content = {"myTitle": title, "products": products}
    return render(request, "mainapp/index.html", content)


def products(request):
    return render(request, "mainapp/products.html")


def contact(request):
    return render(request, "mainapp/contact.html")
