# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from common.models import TimeStampedModel
from autoslug import AutoSlugField
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField
from users.models import User


"""
 Descripcion de modelo para los productos
"""
class Product(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    slug = AutoSlugField(populate_from='name', unique=True)
    description = RichTextField(blank=True, verbose_name='descripción')
    features = RichTextField(blank=True, verbose_name='características')
    price = models.IntegerField(default=0, verbose_name='precio')
    stock = models.IntegerField(default=0)
    img = ImageField(
        upload_to='products/images/',
        null=True,
        blank=True,
        verbose_name='foto'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Productos"
        verbose_name = "Producto"


"""
 Descripcion de modelo para una venta
"""
class Sale(TimeStampedModel):
    total = models.IntegerField(default=0)
    products = models.ManyToManyField(
        Product,
        through='Order',
        verbose_name='productos'
    )
    user = models.ForeignKey(User, verbose_name='usuario')

    def __str__(self):
        return '%s - %s' % (self.user, self.total)

    class Meta:
        verbose_name_plural = "Ventas"
        verbose_name = "Venta"


"""
 Descripcion de modelo para el detalle de la venta (productos vs unidades)
"""
class Order(TimeStampedModel):
    sale = models.ForeignKey(
        Sale,
        verbose_name='venta'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='producto'
    )
    units = models.IntegerField(default=1, verbose_name='unidades')

    def __str__(self):
        return '%s - %s' % (self.sale.pk, self.product.slug)

    class Meta:
        verbose_name_plural = "Pedidos"
        verbose_name = "Pedido"


