# -*- coding: utf-8 -*-
"""
Serializers for the Django REST Framework.
"""

from rest_framework import serializers
from legislative.models import Bill

class BillSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:bill-detail")

    class Meta:
        model = Bill
        fields = (
            'url',
            'id',
            'identifier',
            # 'legislative_session',
            'title',
        )
