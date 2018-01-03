# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from legislative.models import Bill
from general.models import Person
from search_views.filters import BaseFilter
from django.views.generic import TemplateView
from .forms import SearchBillForm

from django.shortcuts import render

# Create your views here.

class BillSearchFilter(BaseFilter):
    search_fields = {
        "search_name" : ["identifier", "title", "lr_number", "legislative_session__name",],
        "search_sessions": { 'operator' : '__exact', 'fields' : ["legislative_session__id",] },
    }


class BillSearchListView(TemplateView):
    model = Bill
    template_name = "search/bill_search_list.html"

class PersonSearchListView(TemplateView):
    model = Person
    template_name = "search/person_search_list.html"

