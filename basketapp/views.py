from django.conf import settings
from django.shortcuts import HttpResponseRedirect, render
from django.http import Http404


def basket(request):
    title = "Корзина"
    basket_items = request.user.user_basket.products.order_by("product__id_cat")
    content = {"title": title, "basket_items": basket_items, "media_url": settings.MEDIA_URL}
    return render(request, "basketapp/basket.html", content)


def basket_add(request, pk):
    if request.user.user_basket.add_product(pk):
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    raise Http404(f'Продукта с id={pk} нет в БД')


def basket_remove(request, pk):
    if request.user.user_basket.remove_product(pk):
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    raise Http404(f'Продукта с id={pk} нет в БД')