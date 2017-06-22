# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.

class EstimateAdmin(admin.ModelAdmin):
    model = Estimate




class CustomerAdmin(admin.ModelAdmin):
    model = Customer


admin.site.register(Estimate, EstimateAdmin)
admin.site.register(Customer, CustomerAdmin)
