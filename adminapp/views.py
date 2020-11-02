from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
from django.urls import reverse

from adminapp.forms import ProductCategoryEditForm, ShopUserAdminEditForm
from authapp.forms import ShopUserRegisterForm
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


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = "пользователи/создание"

    if request.method == "POST":
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse("admin:users"))
    else:
        user_form = ShopUserRegisterForm()

    content = {"title": title, "update_form": user_form, "media_url": settings.MEDIA_URL}

    return render(request, "adminapp/user_update.html", content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = "пользователи/редактирование"

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == "POST":
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("admin:user_update", args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {"title": title, "update_form": edit_form, "media_url": settings.MEDIA_URL}

    return render(request, "adminapp/user_update.html", content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = "пользователи/удаление"

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == "POST":
        # user.delete()
        # Instead delete we will set users inactive
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse("admin:users"))

    content = {"title": title, "user_to_delete": user, "media_url": settings.MEDIA_URL}

    return render(request, "adminapp/user_delete.html", content)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = "админка/категории"
    categories_list = ProductsCategory.objects.all()
    content = {"title": title, "objects": categories_list, "media_url": settings.MEDIA_URL}
    return render(request, "adminapp/categories.html", content)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = "категории/создание"

    if request.method == "POST":
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse("admin:categories"))
    else:
        category_form = ProductCategoryEditForm()

    content = {"title": title, "update_form": category_form, "media_url": settings.MEDIA_URL}

    return render(request, "adminapp/category_update.html", content)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = "категории/редактирование"

    edit_category = get_object_or_404(ProductsCategory, pk=pk)
    if request.method == "POST":
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("admin:category_update", args=[edit_category.pk]))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)

    content = {"title": title, "update_form": edit_form, "media_url": settings.MEDIA_URL}

    return render(request, "adminapp/category_update.html", content)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = "категории/удаление"

    category = get_object_or_404(ProductsCategory, pk=pk)

    if request.method == "POST":
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse("admin:categories"))

    content = {"title": title, "category_to_delete": category, "media_url": settings.MEDIA_URL}

    return render(request, "adminapp/category_delete.html", content)


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = "админка/продукт"
    category = get_object_or_404(ProductsCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by("name")
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