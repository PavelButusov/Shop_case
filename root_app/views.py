# -*- coding: utf-8 -*-
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

from .models import BasketedProduct, Product

# Create your views here.


def _session_key(request):
    session_key = request.session.session_key
    if session_key is None:
        return ''
    return session_key


def _context(request):
    s = _session_key(request)
    basket_count = BasketedProduct.objects.filter(session=s).count()
    return {
        'login_ok': request.user.is_authenticated,
        'basket_count': basket_count,
    }


def index(request):
    return redirect('catalogue')


def login(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # мы определили пользователя. Авторизуем его.
            auth_login(request, user)
            # возвращаем пользователя туда, где был
            pNext = request.POST.get('next', '/')
            return HttpResponseRedirect(pNext)
            # неверная пара логин-пароль
            # не выходим - значит остаёмся на странице авторизации
    return render(request, 'login.html')


def logout(request):
    # очищаем корзину
    candidates = BasketedProduct.objects.filter(session=_session_key(request))
    candidates.delete()

    pNext = request.GET.get('next', '/')
    auth_logout(request)
    return HttpResponseRedirect(pNext)


def catalogue(request):
    context = _context(request)
    context['catalogue'] = Product.objects.all()
    return render(request, 'root_app/catalogue.html', context)


def to_basket(request, product_id):
    session_key = request.session.session_key
    pNext = request.GET.get('next', '/')
    if session_key is None:
        # выводим сообщение "Покупать могут только авторизованные пользователи"
        context = _context(request)
        context['next'] = pNext
        return render(request, 'root_app/need_to_login.html', context)
    # кладём товар в корзину (товар имеет отношение только
    #   к текущему пользователя (сессии))
    try:
        product = Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        raise Http404(u'Вы пытаетесь купить товар, которого нет в каталоге')
    basket_item = BasketedProduct(session=session_key)
    basket_item.save()
    basket_item.product = product_id
    basket_item.save()
    # возвращаем пользователя туда, откуда пришёл
    return HttpResponseRedirect(pNext)


def cleanup_basket(request):
    session_key = request.session.session_key
    pNext = request.GET.get('next', '/')
    if session_key is None:
        return HttpResponseRedirect(pNext)

    candidates = BasketedProduct.objects.filter(session=session_key)
    candidates.delete()
    return HttpResponseRedirect(pNext)


def basket(request):
    products = Product.objects.all()
    basket = []
    for product in products:
        tmp = BasketedProduct.objects.filter(session=_session_key(request),
                                             product=product)
        if tmp.count() > 0:
            basket.append({
                'title': product.title,
                'thumbnail': product.thumbnail,
                'count': tmp.count,
            })

    context = _context(request)
    context['basket'] = basket
    context['basket_is_empty'] = len(basket) == 0
    return render(request, 'root_app/basket.html', context)


def card(request, product_id):
    context = _context(request)
    try:
        product = Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        raise Http404(u'Такого товара нет в каталоге')
    context['product'] = product
    return render(request, 'root_app/card.html', context)
