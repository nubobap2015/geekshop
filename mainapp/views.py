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
            'image_href': '/product/1',  # Почему "/product/1", а не "/products/1"?
            'alt': 'продукт №1',
        },
        {
            'name': 'Стул с клеевым диспенсером',
            'desc': 'НЕ ОТОРВАТЬСЯ!',
            'image_src': 'product-2.jpg',
            'image_href': '/product/2',
            'alt': 'продукт №2',
        },
    ]
    content = {"myTitle": title, "products": products}
    return render(request, "mainapp/index.html", content)


def products(request):
    title = "Продукты"
    links_menu = [
        {"href": "products_all", "name": "все"},
        {"href": "products_home", "name": "дом"},
        {"href": "products_office", "name": "офис"},
        {"href": "products_modern", "name": "модерн"},
        {"href": "products_classic", "name": "классика"},
    ]
    same_products = [
        {"name": "Отличный стул", "desc": "Не оторваться.", "image_src": "product-11.jpg", "alt": "продукт 11"},
        {"name": "Стул повышенного качества", "desc": "Комфортно.", "image_src": "product-21.jpg", "alt": "продукт 21"},
        {"name": "Стул премиального качества", "desc": "Просто попробуйте.", "image_src": "product-31.jpg", "alt": "продукт 31"},
    ]
    content = {"myTitle": title, "links_menu": links_menu, "same_products":same_products}
    return render(request, "mainapp/products.html", content)


def contact(request):
    title = "о нас"
    visit_date = datetime.datetime.now()
    locations = [
        {"city": "Москва", "phone": "+7-888-888-8888", "email": "info@geekshop.ru", "address": "В пределах МКАД"},
        {
            "city": "Екатеринбург",
            "phone": "+7-777-777-7777",
            "email": "info_yekaterinburg@geekshop.ru",
            "address": "Близко к центру",
        },
        {
            "city": "Владивосток",
            "phone": "+7-999-999-9999",
            "email": "info_vladivostok@geekshop.ru",
            "address": "Близко к океану",
        },
    ]
    content = {"myTitle": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contact.html", content)
