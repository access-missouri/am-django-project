# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Bill

class BillDetailView(DetailView):
    model = Bill
    context_object_name = "bill"
    template_name = 'legislative/bill_detail.html'

    def get_object(self):
        if self.kwargs['id']:
            return Bill.objects.get(id=self.kwargs['id'])
        return super(BillDetailView, self).get_objects()

