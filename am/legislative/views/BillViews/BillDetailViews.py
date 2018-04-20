# -*- coding: utf-8 -*-
"""
Legislative views.
"""
from __future__ import unicode_literals

from django.views.generic import DetailView, ListView
from legislative.models import Bill, BillVote, BillText, LegislativeSession, BillAction


class BillDetailView(DetailView):
    """
    View showing detail information about an individual bill.
    """

    model = Bill
    context_object_name = "bill"
    template_name = 'legislative/bill_detail.html'

    def get_object(self):
        """
        Retrieves object based on ID.
        """
        if self.kwargs['id']:
            return Bill.objects.get(id=self.kwargs['id'])
        return super(BillDetailView, self).get_objects()

class BillVotesListView(DetailView):
    """
    View showing all of an individual bill's votes.
    """

    model = Bill
    context_object_name = "bill"
    template_name = 'legislative/bill_votes_list.html'

    def get_object(self):
        """
        Retrieves object based on ID.
        """
        if self.kwargs['id']:
            return Bill.objects.get(id=self.kwargs['id'])
        return super(BillVotesListView, self).get_objects()


class BillTextDetailView(DetailView):
    """
    View showing detail information about an individual bill text.
    """

    model = BillText
    context_object_name = "text"
    template_name = 'legislative/bill_text_detail.html'

    def get_object(self):
        """
        Retrieves object based on ID.
        """
        if self.kwargs['id']:
            return BillText.objects.get(id=self.kwargs['id'])
        return super(BillTextDetailView, self).get_objects()
