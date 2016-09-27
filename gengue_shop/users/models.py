# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class User(AbstractUser):
    # additional fields here

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Usuarios"
        verbose_name = "Usuario"
