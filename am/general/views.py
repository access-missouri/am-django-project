# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import DetailView
from .models import Person

class PersonDetailView(DetailView):
    model = Person
    context_object_name = "person"
    template_name = 'general/person_detail.html'

    def get_object(self):
        if self.kwargs['id']:
            return Person.objects.get(id=self.kwargs['id'])
        return super(PersonDetailView, self).get_objects()

