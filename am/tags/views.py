# -*- coding: utf-8 -*-
"""
Tag views.
"""
from __future__ import unicode_literals

from django.views.generic import DetailView
from legislative.models import Bill, BillAction
from general.models import Tag


class TagDetailView(DetailView):
    model = Tag
    context_object_name = "tag"
    template_name = 'tags/tag_detail.html'

    def get_object(self):
        """
        Retrieves object based on slug.
        """
        if self.kwargs['slug']:
            return Tag.objects.get(slug=self.kwargs['slug'])
        return super(TagDetailView, self).get_object()

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        this = self.get_object()
        context['bills'] = Bill.objects.filter(tags=this)[:25]
        context['bill_actions'] = BillAction.objects.filter(bill__tags=this)[:25]
        return context
