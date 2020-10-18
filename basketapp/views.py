from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render
from django.http import Http404

@login_required
def basket(request):
    title = "Корзина"
    basket_items = request.user.products.order_by("product__id_cat")
    content = {"title": title, "basket_items": basket_items, "media_url": settings.MEDIA_URL}
    return render(request, "basketapp/basket.html", content)

@login_required
def basket_add(request, pk):
    if request.user.add_product(pk):
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    raise Http404(f'Продукта с id={pk} нет в БД')

@login_required
def basket_remove(request, pk):
    if request.user.remove_product(pk):
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    raise Http404(f'Продукта с id={pk} нет в БД')