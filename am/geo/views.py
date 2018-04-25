# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView
from geo import models

# Create your views here.

class DistrictDetailView(DetailView):
    """
    View showing detail information about an individual district.
    """

    model = models.District
    context_object_name = "district"
    template_name = 'geo/district_detail.html'

    def get_object(self):
        """
        Retrieves object based on ID.
        """
        if self.kwargs['id']:
            return models.District.objects.get(id=self.kwargs['id'])
        return super(DistrictDetailView, self).get_objects()
