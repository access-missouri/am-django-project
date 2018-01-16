# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView, ListView
from .models import FinanceEntity, FinanceTransaction

# Create your views here.

class FinanceHomeView(ListView):
    queryset = FinanceTransaction.objects.all()[:25]
    context_object_name = "transactions"
    model = FinanceTransaction
    template_name = "finance/finance_overview.html"

    def get_context_data(self, **kwargs):
        context = super(FinanceHomeView, self).get_context_data(**kwargs)
        return context

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

class EntityDetailIncomeListView(DetailView):
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
