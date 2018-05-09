#!/usr/bin/env python
# -*- coding: utf-8 -*-
from graphene import relay, ObjectType, String
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from legislative import models as LM

class BillNode(DjangoObjectType):
    absolute_url = String()
    admin_url = String()
    bill_status_text = String()

    def resolve_absolute_url(instance, info, **kwargs):
        return instance.get_absolute_url()
    
    def resolve_admin_url(instance, info, **kwargs):
        return instance.get_admin_url()

    def resolve_bill_Status(instance, info, **kwargs):
        return instance.get_bill_status()

    class Meta:
        model = LM.Bill
        filter_fields = {
            'identifier': ['exact', 'icontains', 'istartswith'],
            'legislative_session__name': ['exact', 'icontains', 'istartswith'],
            'from_organization__name': ['exact', 'icontains', 'istartswith'],
            'title': ['exact', 'icontains', 'istartswith'],
            'lr_number': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class BillActionNode(DjangoObjectType):

    class Meta:
        model = LM.BillAction
        filter_fields = {
            'bill__identifier': ['exact', 'icontains', 'istartswith'],
            'bill__title': ['exact', 'icontains', 'istartswith'],
            'organization__name': ['exact', 'icontains', 'istartswith'],
            'date': ['year', 'month', 'day'],
        }
        interfaces = (relay.Node,)

class BillSponsorshipNode(DjangoObjectType):

    class Meta:
        model = LM.BillSponsorship
        filter_fields = {
            'bill__identifier': ['exact', 'icontains', 'istartswith'],
            'bill__title': ['exact', 'icontains', 'istartswith'],
            'person__index_name': ['exact', 'icontains', 'istartswith'],
            'member__person': ['exact'],
            'member__session': ['exact'],
            'member__session__name': ['exact', 'icontains', 'istartswith'],
            'sponsored_at': ['year', 'month', 'day'],
        }
        interfaces = (relay.Node,)

class LegislativeSessionNode(DjangoObjectType):
    absolute_url = String()

    def resolve_absolute_url(instance, info, **kwargs):
        return instance.get_absolute_url()

    class Meta:
        model = LM.LegislativeSession
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'classification': ['exact', 'icontains', 'istartswith'],
            'start_date': ['year', 'month', 'day'],
            'end_date': ['year', 'month', 'day'],
        }
        interfaces = (relay.Node,)

class BodyMembershipNode(DjangoObjectType):
    absolute_url = String()

    def resolve_absolute_url(instance, info, **kwargs):
        return instance.get_absolute_url()

    class Meta:
        model = LM.BodyMembership
        filter_fields = {
            'person__index_name': ['exact', 'icontains', 'istartswith'],
            'person__first_name': ['exact', 'icontains', 'istartswith'],
            'person__last_name': ['exact', 'icontains', 'istartswith'],
            'person__suffix': ['exact', 'icontains', 'istartswith'],
            'body': ['exact', 'icontains', 'istartswith'],
            'session__name': ['exact', 'icontains', 'istartswith'],
            'district__name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)



class Query(object):
    bill = relay.Node.Field(BillNode)
    all_bills = DjangoFilterConnectionField(BillNode)

    bill_action = relay.Node.Field(BillActionNode)
    all_bill_actions = DjangoFilterConnectionField(BillActionNode)

    legislative_session = relay.Node.Field(LegislativeSessionNode)
    all_legislative_sessions = DjangoFilterConnectionField(LegislativeSessionNode)

    body_membership = relay.Node.Field(BodyMembershipNode)
    all_body_memberships = DjangoFilterConnectionField(BodyMembershipNode)

