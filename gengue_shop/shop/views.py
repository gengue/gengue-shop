# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core import serializers

from users.models import User
from .models import Product, Sale, Order



class HomeView(View):
    template_name='pages/home.html'

    def get(self, request, *args, **kwargs):
        context = {}
        products = Product.objects.all()
        context['products_json'] = serializers.serialize('json', products)

        if not self.request.user.is_anonymous():
            context['user_json'] = serializers.serialize('json', products)

        paginator = Paginator(products , 8)
        page = request.GET.get('page')
        try:
            context['products'] = paginator.page(page)
        except PageNotAnInteger:
            context['products'] = paginator.page(1)
        except EmptyPage:
            context['products'] = paginator.page(paginator.num_pages)

        return render(request, self.template_name, context)


class ProductDetailView(DetailView):
    template_name='pages/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['products_json'] = serializers.serialize('json', Product.objects.all())
        if not self.request.user.is_anonymous():
            context['user_json'] = serializers.serialize('json', [self.request.user])
        return context


@method_decorator(csrf_exempt, name='dispatch')
class CheckoutView(View):
    template_name='pages/checkout.html'

    def get(self, request, *args, **kwargs):
        context = {}
        products = Product.objects.all()
        context['products_json'] = serializers.serialize('json', products)

        if request.user:
            context['user_json'] = serializers.serialize('json', products)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        cart_unicode = request.body.decode('utf-8')
        cart = json.loads(cart_unicode)
        if request.user.is_authenticated():
            sale = Sale(user=request.user)
            sale.save()
            total = 0
            for item in cart['products']:
                product = Product.objects.get(pk=item['id'])
                order = Order.objects.create(
                    product_id=product.pk,
                    sale_id=sale.pk,
                    units=item['units']
                )
                total += product.price*order.units
                product.stock -= order.units
                product.save()
            sale.total = total
            sale.save()
            response = {'msg': 'ok', 'status': 201 }
        else:
            response = {'msg': 'Usuario no autenticado', 'status': 403}
        return JsonResponse(response)




