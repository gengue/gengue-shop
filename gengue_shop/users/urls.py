# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^login/$', views.auth_login, name='auth_login'),
    url(r'^register/$', views.auth_register, name='auth_register'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="auth_logout"),
]
