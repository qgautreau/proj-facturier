# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import AppUser, Customer, Proposal
from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView

# Create your views here.

def homepage(request):
    return render(request, "homepage.html")


class AppUserDetailView(DetailView):
    model = AppUser
    slug_field = "company"


class CustomerListView(ListView):
    model = Customer
    context_object_name = "customers"


class ProposalListView(ListView):
    model = Proposal
    context_object_name = "proposals"


class ProposalDetailView(DetailView):
    model = Proposal
    slug_field = "ref"
