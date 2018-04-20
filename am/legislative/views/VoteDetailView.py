# -*- coding: utf-8 -*-
"""
Legislative views.
"""
from __future__ import unicode_literals

from django.views.generic import DetailView
from legislative.models import BillVote

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