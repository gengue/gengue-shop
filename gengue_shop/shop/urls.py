# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^producto/(?P<slug>[\w-]+)/$', views.ProductDetailView.as_view(), name='product-detail'),
    url(r'^comprar/$', views.CheckoutView.as_view(), name='checkout'),
]
