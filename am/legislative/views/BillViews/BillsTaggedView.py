# -*- coding: utf-8 -*-
"""
Legislative views.
"""
from __future__ import unicode_literals

from django.views.generic import DetailView
from legislative.models import Bill, BillAction
from general.models import Tag


class BillsTaggedView(DetailView):
    model = Tag
    context_object_name = "tag"
    template_name = 'legislative/bills_tagged.html'

    def get_object(self):
        """
        Retrieves object based on slug.
        """
        if self.kwargs['slug']:
            return Tag.objects.get(slug=self.kwargs['slug'])
        return super(BillsTaggedView, self).get_object()

    def get_context_data(self, **kwargs):
        context = super(BillsTaggedView, self).get_context_data(**kwargs)
        context['bills'] = Bill.objects.filter(tags=self.get_object())[:25]
        return context
