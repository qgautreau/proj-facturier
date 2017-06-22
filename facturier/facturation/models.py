# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    company = models.CharField(verbose_name="company",max_length=50, )
    first_name = models.CharField(verbose_name="", max_length=50, )
    last_name = models.CharField(verbose_name="", max_length=50, )
    siret = models.IntegerField(verbose_name="", max_length=14, )
    phone = models.IntegerField(verbose_name="phone", max_length=10, null=True)
    mail = models.CharField(max_length=20, null=True)
    address_1 = models.CharField(max_length=30, verbose_name="address 1", null=True)
    address_2 = models.CharField(max_length=30, verbose_name="address 2", null=True)
    zip_code = models.IntegerField(verbose_name= "zipcode", null=True)
    city = models.CharField(max_length=30, verbose_name="city", null=True)
    country = models.CharField(max_length=30, verbose_name="country", null=True)


class Customer(models.Model):
    company = models.CharField(verbose_name="company", max_length=50, )
    first_name = models.CharField(verbose_name="first name", max_length=50, )
    last_name = models.CharField(verbose_name="last name", max_length=50, )
    siret = models.IntegerField(verbose_name="SIRET", )
    phone = models.IntegerField(verbose_name="phone", max_length=10, null=True)
    mail = models.CharField(max_length=20, null=True)
    address_1 = models.CharField(max_length=30, verbose_name="address 1", null=True)
    address_2 = models.CharField(max_length=30, verbose_name="address 2", null=True)
    zip_code = models.IntegerField(verbose_name= "zipcode", null=True)
    city = models.CharField(max_length=30, verbose_name="city", null=True)
    country = models.CharField(max_length=30, verbose_name="country", null=True)


class Estimate(models.Model):    user = models.ForeignKey("User")
    customer = models.ForeignKey("Customer")
    ref = models.CharField(verbose_name="reference", max_length=50, )
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    amount = models.FloatField(verbose_name="amount", )
    refusal_date = models.DateTimeField(null=True, blank=True)
    acceptance_date = models.DateTimeField(null=True, blank=True)


class Bill(models.Model):
    user = models.ForeignKey("User")
    customer = models.ForeignKey("Customer")
    ref = models.CharField(verbose_name="reference", max_length=50, )
    date = models.DateField(verbose_name="date", )
    amount = models.FloatField(verbose_name="amount", )


class Product(models.Model):
    name = models.CharField(verbose_name="name", max_length=50, )
    price = models.CharField(verbose_name="price", max_length=50, )
    qty = models.CharField(verbose_name="quantity", max_length=50, )
