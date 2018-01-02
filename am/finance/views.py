# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView
from .models import FinanceEntity

# Create your views here.
class EntityDetailView(DetailView):
    """
    View showing detail information about an individual finance entity.
    """

    model = FinanceEntity
    context_object_name = "object"
    template_name = 'finance/entity_detail.html'

    def get_object(self):
        """
        Retrieves object based on ID.
        """
        if self.kwargs['id']:
            return FinanceEntity.objects.get(id=self.kwargs['id'])
        return super(EntityDetailView, self).get_objects()

class EntityDetailSpendingListView(DetailView):
    """
    View showing detail information about an individual finance entity.
    """

    model = FinanceEntity
    context_object_name = "object"
    template_name = 'finance/entity_detail_spend_list.html'

    def get_object(self):
        """
        Retrieves object based on ID.
        """
        if self.kwargs['id']:
            return FinanceEntity.objects.get(id=self.kwargs['id'])
        return super(EntityDetailView, self).get_objects()