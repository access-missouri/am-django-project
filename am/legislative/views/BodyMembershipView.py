# -*- coding: utf-8 -*-
"""
Legislative views.
"""
from __future__ import unicode_literals

from django.views.generic import DetailView, ListView
from legislative.models import BodyMembership

class BodyMembershipView(DetailView):
    """
    View showing detail information about a single body membership in a legislative Session.
    """

    model = BodyMembership
    context_object_name = "membership"
    template_name = 'legislative/body_membership_detail.html'

    def get_object(self):
        """
        Retrieves object based on ID.
        """
        if self.kwargs['id']:
            return BodyMembership.objects.get(id=self.kwargs['id'])
        return super(BodyMembershipView, self).get_objects()

class BodyMembershipVotesView(DetailView):
    model = BodyMembership
    context_object_name = "membership"
    template_name = 'legislative/body_membership_votes.html'

    def get_object(self):
        """
        Retrieves object based on ID.
        """
        if self.kwargs['id']:
            return BodyMembership.objects.get(id=self.kwargs['id'])
        return super(BodyMembershipView, self).get_object()

    def get_context_data(self, **kwargs):
        context = super(BodyMembershipVotesView, self).get_context_data(**kwargs)
        context['votes'] = self.get_object().votes.select_related('bill_vote', 'bill_vote__bill').all()
        return context