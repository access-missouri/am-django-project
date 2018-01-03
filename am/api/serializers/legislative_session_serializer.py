# -*- coding: utf-8 -*-
"""
Serializers for the Django REST Framework.
"""

from rest_framework import serializers
from legislative.models import LegislativeSession

class LegislativeSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegislativeSession
        fields = ('name', 'id')
