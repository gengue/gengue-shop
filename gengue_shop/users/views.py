# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render

from .models import User


def auth_login(request):
    next_url = request.GET.get('next', None)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        url = next_url if next_url else '/'
        return redirect(url)
    else:
        return render(request, 'pages/home.html', {})


def auth_register(request):
    next_url = request.GET.get('next', None)
    user = User.objects.create(
             username=request.POST['username'],
             email=request.POST['email'],
             first_name=request.POST['first_name'],
             last_name=request.POST['last_name']
    )
    user.set_password(request.POST['password'])
    user.save()
    user = authenticate(
        username=request.POST['username'], password=request.POST['password']
    )
    login(request, user)
    url = next_url if next_url else '/'
    return redirect(url)

