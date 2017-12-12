# -*- coding: utf-8 -*-
"""
Serializers for the Django REST Framework.
"""

from rest_framework import serializers
from legislative.models import Bill, LegislativeSession

class LegislativeSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegislativeSession
        fields = ('name', 'id')

class BillSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:bill-detail")
    # display_name = serializers.CharField()
    legislative_session = LegislativeSessionSerializer(read_only=True)

    class Meta:
        model = Bill
        fields = (
            'url',
            'id',
            # 'display_name',
            'identifier',
            'legislative_session',
            'title',
        )

