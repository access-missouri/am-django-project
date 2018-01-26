# -*- coding: utf-8 -*-
"""
Serializers for the Django REST Framework.
"""

from rest_framework import serializers
from finance.models import FinanceEntity

class BillSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:bill-detail")

    class Meta:
        model = FinanceEntity
        fields = (
            'url',
            'id',
            'name',
        )

