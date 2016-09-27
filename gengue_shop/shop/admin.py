# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from .models import Product, Sale, Order



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('get_img', 'name', 'get_price', 'stock',)

    def get_img(self, obj):
        source = obj.img.url if obj.img else 'http://directory.africa-business.com/assets/media/noimage.png'
        return """ <img src="{0}" height="60">""".format(source)

    get_img.allow_tags = True
    get_img.short_description = 'Imagen'
    get_img.order_field = 'pk'

    def get_price(self, obj):
        return '$ %.2f' % obj.price

    get_img.short_description = 'Precio'
    get_img.order_field = 'price'


@admin.register(Sale)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_products', 'created', 'get_total',)
    search_fields = ('user__first_name', 'user__last_name', 'user__username',
                     'products__name', 'created')

    def get_total(self, obj):
        return '$ %.2f' % obj.total

    get_total.short_description = 'Total'
    get_total.order_field = 'total'

    def get_products(self, obj):
        html = '<ul>'
        for order in obj.order_set.all():
            html += '<li>'
            html += order.product.name + '({0})'.format(order.units)
            html += '</li>'
        html += '</ul>'
        return html

    get_products.allow_tags = True
    get_products.short_description = 'Productos'
