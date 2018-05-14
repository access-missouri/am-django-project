# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, generics
from api.serializers import *
from finance.models import FinanceEntity
from search.utils import request_params_to_q_set_query

# Create your views here.
class FinanceEntityAPIViewset(viewsets.ReadOnlyModelViewSet):
    """
    Currently allows viewing /and/ editing of bills. Must be fixed.
    """
    queryset = FinanceEntity.objects.all()
    serializer_class = FinanceEntitySerializer

class FinanceEntitySearchAPIView(generics.ListAPIView):
    """
    Optionally takes your search query in the form of URL parameters.
    accessmo.org/api/financeentities/?[attribute]_search=[search here]
    """
    serializer_class = FinanceEntitySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned bills by search query.
        """
        queryset = FinanceEntity.objects.all()
        if self.request.query_params:
            query = request_params_to_q_set_query(self.request.query_params)
            queryset = queryset.filter(query)
        return queryset
