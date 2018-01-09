# -*- coding: utf-8 -*-
"""
Views and rendering systems from AM general.
"""
from __future__ import unicode_literals
from braces.views import SelectRelatedMixin
from django.views.generic import DetailView, ListView
from .models import Person
from legislative.models import Bill, PersonVote
from finance.models import FinanceTransaction
from django.shortcuts import render_to_response, render
from django.template import RequestContext


def handler404(request):
    response = render_to_response('errors/404.html')
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('errors/500.html')
    response.status_code = 500
    return response


class HomePageView(ListView):
    """
    The site home page.
    """

    model = Bill
    queryset = Bill.objects.all()

    template_name = "general/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['people'] = Person.objects.all()
        context['bills'] = Bill.objects.all()
        context['personvotes'] = PersonVote.objects.all()
        context['finance_transactions'] = FinanceTransaction.objects.filter(amount__gte=500)[:5]
        return context

class PersonDetailView(DetailView):
    """
    Individual person profile view.
    """

    model = Person
    context_object_name = "person"
    template_name = 'general/person_detail.html'

    def get_object(self):
        """
        Get based on ID.

        :return:
        """
        if self.kwargs['id']:
            return Person.objects.get(id=self.kwargs['id'])
        return super(PersonDetailView, self).get_objects()


class PersonVotesListView(SelectRelatedMixin, DetailView):
    """
    Individual person profile view.
    """

    model = Person
    context_object_name = "person"
    select_related = ['bills']
    template_name = 'general/person_votes_list.html'

    def get_object(self):
        """
        Get based on ID.

        :return:
        """
        if self.kwargs['id']:
            return Person.objects.get(id=self.kwargs['id'])
        return super(PersonVotesListView, self).get_objects()