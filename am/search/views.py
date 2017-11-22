# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from legislative.models import Bill
from search_views.filters import BaseFilter
from search_views.views import SearchListView
from .forms import SearchBillForm

from django.shortcuts import render

# Create your views here.

class BillSearchFilter(BaseFilter):
    search_fields = {
        "search_name" : ["identifier", "title", "lr_number", "legislative_session__name",],
        "search_sessions": { 'operator' : '__exact', 'fields' : ["legislative_session__id",] },
    }


class BillSearchListView(SearchListView):
    model = Bill
    paginate_by = 50
    template_name = "search/bill_search_list.html"

    form_class = SearchBillForm
    filter_class = BillSearchFilter
