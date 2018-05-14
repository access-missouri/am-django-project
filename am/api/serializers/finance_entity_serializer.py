# -*- coding: utf-8 -*-
"""
Serializers for the Django REST Framework.
"""

from rest_framework import serializers
from finance.models import FinanceEntity

class FinanceEntitySerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:financeentity-detail")

    class Meta:
        model = FinanceEntity
        fields = (
            'url',
            'id',
            'name',
        )

