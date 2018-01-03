# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, generics
from api.serializers import *
from general.models import Person
from search.utils import request_params_to_q_set_query

# Create your views here.
class PersonAPIViewset(viewsets.ReadOnlyModelViewSet):
    """
    Currently allows viewing /and/ editing of bills. Must be fixed.
    """
    queryset = Person.objects.all()
    serializer_class = BillSerializer

class PersonSearchAPIView(generics.ListAPIView):
    """
    Optionally takes your search query in the form of URL parameters.
    accessmo.org/api/people/?[attribute]_search=[search here]
    """
    serializer_class = PersonSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned bills by search query.
        """
        queryset = Person.objects.all()
        if self.request.query_params:
            query = request_params_to_q_set_query(self.request.query_params)
            queryset = queryset.filter(query)
        return queryset