# -*- coding: utf-8 -*-
"""
Serializers for the Django REST Framework.
"""

from rest_framework import serializers
from general.models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:person-detail")

    class Meta:
        model = Person
        fields = (
            'url',
            'first_name',
            'middle_name',
            'last_name',
            'nickname',
            'suffix',
            'gender',
            'index_name',
        )

