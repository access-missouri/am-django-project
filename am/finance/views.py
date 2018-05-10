# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView, ListView
from .models import FinanceEntity, FinanceTransaction
from django.db.models import Sum

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

    def get_context_data(self, **kwargs):
        context = super(EntityDetailView, self).get_context_data(**kwargs)
        this = self.get_object()
        context['top_donors'] = this.income.values('t_from__name','t_from__id', 't_from__e_type').annotate(amount=Sum('amount')).order_by('-amount')[:5]
        context['top_targets'] = this.spending.values('t_to__name','t_to__id', 't_to__e_type').annotate(amount=Sum('amount')).order_by('-amount')[:5]
        return context

class TransactionDetailView(DetailView):
    """
    View showing detail information about an individual transaction.
    """

    model = FinanceTransaction
    context_object_name = "object"
    template_name = 'finance/transaction_detail.html'

    def get_object(self):
        """
        Retrieves object based on ID.
        """
        if self.kwargs['id']:
            return FinanceTransaction.objects.get(id=self.kwargs['id'])
        return super(TransactionDetailView, self).get_objects()

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
    template_name = 'finance/entity_detail_income_list.html'

    def get_object(self):
        """
        Retrieves object based on ID.
        """
        if self.kwargs['id']:
            return FinanceEntity.objects.get(id=self.kwargs['id'])
        return super(EntityDetailView, self).get_objects()
