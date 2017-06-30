# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from models import *

# Register your models here.

class ProposalAdmin(admin.ModelAdmin):
    model = Proposal


class CustomerAdmin(admin.ModelAdmin):
    model = Customer


class AppUserInline(admin.StackedInline):
    model = AppUser
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (AppUserInline, )

admin.site.unregister(User)

admin.site.register(Proposal, ProposalAdmin)
admin.site.register(Status)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(User, UserAdmin)
