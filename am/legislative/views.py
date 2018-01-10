# -*- coding: utf-8 -*-
"""
Legislative views.
"""
from __future__ import unicode_literals

from django.views.generic import DetailView, ListView
from .models import Bill, BillVote, BillText, LegislativeSession, BillAction


class BillsHomeView(ListView):
    queryset = BillAction.objects.all()[:25]
    context_object_name = "actions"
    model = BillAction
    template_name = "legislative/bills_overview.html"

    def get_context_data(self, **kwargs):
        context = super(BillsHomeView, self).get_context_data(**kwargs)
        context['bills'] = Bill.objects.all()[:25]
        return context

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


class VoteDetailView(DetailView):
    """
    View showing detail information about an individual vote (BillVote).
    """

    model = BillVote
    context_object_name = "vote"
    template_name = 'legislative/vote_detail.html'

    def get_object(self):
        """
        Retrieves object based on ID.
        """
        if self.kwargs['id']:
            return BillVote.objects.get(id=self.kwargs['id'])
        return super(VoteDetailView, self).get_objects()

class LegislativeSessionView(DetailView):
    """
    View showing detail information about a single Legislative Session.
    """

    model = LegislativeSession
    context_object_name = "session"
    template_name = 'legislative/session_detail.html'

    def get_object(self):
        """
        Retrieves object based on ID.
        """
        if self.kwargs['id']:
            return LegislativeSession.objects.get(id=self.kwargs['id'])
        return super(VoteDetailView, self).get_objects()

class LegislativeSessionListView(ListView):
    """
    View showing a list of all legislative session objects.
    """

    model = LegislativeSession
    queryset = LegislativeSession.objects.all()
    context_object_name = "sessions"
    ordering = "name"
    template_name = 'legislative/session_list.html'