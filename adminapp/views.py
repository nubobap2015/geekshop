from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from authapp.models import ShopUser
from mainapp.models import Product, ProductsCategory


@user_passes_test(lambda u: u.is_superuser)
def admin_main(request):
    response = redirect("admin:users")
    return response


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = "админка/пользователи"
    users_list = ShopUser.objects.all().order_by("-is_active", "-is_superuser", "-is_staff", "username")
    content = {"title": title, "objects": users_list, "media_url": settings.MEDIA_URL}
    return render(request, "adminapp/users.html", content)


def user_create(request):
    response = redirect("admin:users")
    return response


def user_update(request, pk):
    response = redirect("admin:users")
    return response


def user_delete(request, pk):
    response = redirect("admin:users")
    return response


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = "админка/категории"
    categories_list = ProductsCategory.objects.all()
    content = {"title": title, "objects": categories_list, "media_url": settings.MEDIA_URL}
    return render(request, "adminapp/categories.html", content)


def category_create(request):
    response = redirect("admin:categories")
    return response


def category_update(request, pk):
    response = redirect("admin:categories")
    return response


def category_delete(request, pk):
    response = redirect("admin:categories")
    return response


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = "админка/продукт"
    category = get_object_or_404(ProductsCategory, pk=pk)
    products_list = Product.objects.filter(id_cat__pk=pk).order_by("name")
    content = {"title": title, "category": category, "objects": products_list, "media_url": settings.MEDIA_URL}
    return render(request, "adminapp/products.html", content)


def product_create(request, pk):
    response = redirect("admin:categories")
    return response


def product_read(request, pk):
    response = redirect("admin:categories")
    return response


def product_update(request, pk):
    response = redirect("admin:categories")
    return response


def product_delete(request, pk):
    response = redirect("admin:categories")
    return response
