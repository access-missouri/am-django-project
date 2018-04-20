# -*- coding: utf-8 -*-
"""
Legislative views.
"""
from __future__ import unicode_literals

from django.views.generic import DetailView, ListView
from legislative.models import LegislativeSession

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
        return super(LegislativeSessionView, self).get_objects()

class LegislativeSessionListView(ListView):
    """
    View showing a list of all legislative session objects.
    """

    model = LegislativeSession
    queryset = LegislativeSession.objects.all()
    context_object_name = "sessions"
    ordering = "name"
    template_name = 'legislative/session_list.html'