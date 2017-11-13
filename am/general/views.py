# -*- coding: utf-8 -*-
"""
Views and rendering systems from AM general.
"""
from __future__ import unicode_literals

from django.views.generic import DetailView
from .models import Person


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
