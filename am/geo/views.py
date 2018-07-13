# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import DetailView
from geo import models
from django.db.models import ObjectDoesNotExist
from django.http import Http404

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
        try:
            if self.kwargs['id']:
                return models.District.objects.get(id=self.kwargs['id'])
        except ObjectDoesNotExist:
            raise Http404
