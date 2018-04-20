# -*- coding: utf-8 -*-
"""
Legislative views.
"""
from __future__ import unicode_literals

from django.views.generic import ListView
from legislative.models import Bill, BillAction


class BillsHomeView(ListView):
    queryset = BillAction.objects.all()[:25]
    context_object_name = "actions"
    model = BillAction
    template_name = "legislative/bills_overview.html"

    def get_context_data(self, **kwargs):
        context = super(BillsHomeView, self).get_context_data(**kwargs)
        context['bills'] = Bill.objects.all()[:25]
        return context

