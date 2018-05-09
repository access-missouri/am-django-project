#!/usr/bin/env python
# -*- coding: utf-8 -*-
from graphene import relay, ObjectType, String
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from general.models import Person, Organization

class PersonNode(DjangoObjectType):
    absolute_url = String()
    full_name = String()
    admin_url = String()

    def resolve_absolute_url(instance, info, **kwargs):
        return instance.get_absolute_url()

    def resolve_full_name(instance, info, **kwargs):
        return instance.get_full_name()

    def resolve_admin_url(instance, info, **kwargs):
        return instance.get_admin_url()

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
