#!/usr/bin/env python
# -*- coding: utf-8 -*-
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from general.models import Person, Organization

class PersonNode(DjangoObjectType):
    class Meta:
        model = Person
        filter_fields = {
            'index_name': ['exact', 'icontains', 'istartswith'],
            'first_name': ['exact', 'icontains', 'istartswith'],
            'middle_name': ['exact', 'icontains', 'istartswith'],
            'suffix': ['exact', 'icontains', 'istartswith'],
            'gender': ['exact', 'icontains', 'istartswith'],
            'nickname': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

class OrganizationNode(DjangoObjectType):
    class Meta:
        model = Organization
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'parent__name': ['exact', 'icontains', 'istartswith'],
            'classification': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class Query(object):
    person = relay.Node.Field(PersonNode)
    all_people = DjangoFilterConnectionField(PersonNode)

    organization = relay.Node.Field(OrganizationNode)
    all_organizations = DjangoFilterConnectionField(OrganizationNode)