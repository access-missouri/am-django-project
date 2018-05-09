#!/usr/bin/env python
# -*- coding: utf-8 -*-
from graphene import relay, ObjectType, String
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from finance.models import FinanceEntity, FinanceTransaction


class FinanceEntityNode(DjangoObjectType):
    absolute_url = String()

    def resolve_absolute_url(instance, info, **kwargs):
        return instance.get_absolute_url()

    class Meta:
        model = FinanceEntity
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

class FinanceTransactionNode(DjangoObjectType):
    absolute_url = String()

    def resolve_absolute_url(instance, info, **kwargs):
        return instance.get_absolute_url()

    class Meta:
        model = FinanceTransaction
        filter_fields = {
            't_from': ['exact'],
            't_to': ['exact'],
            't_from__name': ['exact', 'icontains', 'istartswith'],
            't_to__name': ['exact', 'icontains', 'istartswith'],
            'amount': ['exact', 'gt', 'gte', 'lt', 'lte'],
        }
        interfaces = (relay.Node,)

class Query(object):
    finance_entity = relay.Node.Field(FinanceEntityNode)
    all_finance_entities = DjangoFilterConnectionField(FinanceEntityNode)

    finance_transaction = relay.Node.Field(FinanceTransactionNode)
    all_finance_transactions = DjangoFilterConnectionField(FinanceTransactionNode)
