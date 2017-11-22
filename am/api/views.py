# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from legislative.models import Bill
from search.utils import request_params_to_filter_dict

# Create your views here.
class BillAPIViewset(viewsets.ReadOnlyModelViewSet):
    """
    Currently allows viewing /and/ editing of bills. Must be fixed.
    """
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillSearchAPIView(generics.ListAPIView):
    """
    Optionally takes your search query in the form of URL parameters.
    accessmo.org/api/bills/?[attribute]_search=[search here]
    """
    serializer_class = BillSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned bills by search query.
        """
        queryset = Bill.objects.all()
        if self.request.query_params:
            filter_dict = request_params_to_filter_dict(self.request.query_params)
            queryset = queryset.filter(**filter_dict)
        return queryset