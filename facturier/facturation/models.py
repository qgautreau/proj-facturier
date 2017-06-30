# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="user")
    company = models.CharField(verbose_name="company",max_length=50, )
    siret = models.IntegerField(verbose_name="", max_length=14, )
    phone = models.IntegerField(verbose_name="phone", max_length=10, null=True)
    mail = models.CharField(verbose_name="Email", max_length=30, null=True)
    address_1 = models.CharField(max_length=30, verbose_name="address 1", null=True)
    address_2 = models.CharField(max_length=30, verbose_name="address 2", null=True)
    zip_code = models.IntegerField(verbose_name= "zipcode", null=True)
    city = models.CharField(max_length=30, verbose_name="city", null=True)
    country = models.CharField(max_length=30, verbose_name="country", null=True)

    def __unicode__(self):
        return self.user


class Customer(models.Model):
    company = models.CharField(verbose_name="company", max_length=50, )
    first_name = models.CharField(verbose_name="first name", max_length=50, )
    last_name = models.CharField(verbose_name="last name", max_length=50, )
    siret = models.IntegerField(verbose_name="SIRET", )
    phone = models.IntegerField(verbose_name="phone", max_length=10, null=True)
    mail = models.CharField(verbose_name="Email", max_length=30, null=True)
    address_1 = models.CharField(max_length=30, verbose_name="address 1", null=True)
    address_2 = models.CharField(max_length=30, verbose_name="address 2", null=True)
    zip_code = models.IntegerField(verbose_name= "zipcode", null=True)
    city = models.CharField(max_length=30, verbose_name="city", null=True)
    country = models.CharField(max_length=30, verbose_name="country", null=True)

    def __unicode__(self):
        return self.company


class Status(models.Model):
    label = models.CharField(max_length=20,)

    def __unicode__(self):
       return self.label

    class Meta:
        verbose_name_plural = "Status"


class Proposal(models.Model):
    customer = models.ForeignKey(Customer)
    appuser = models.ForeignKey(AppUser)
    status = models.ForeignKey(Status)
    ref = models.CharField(max_length=20, unique=True, verbose_name="reference")
    creation_date = models.DateTimeField(auto_now_add=True)
    refusal_date = models.DateTimeField(null=True, blank=True)
    acceptance_date = models.DateTimeField(null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.ref
