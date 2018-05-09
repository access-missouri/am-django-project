#!/usr/bin/env python
# -*- coding: utf-8 -*-
import graphene
from graphene_django.types import DjangoObjectType
from finance.models import FinanceEntity, FinanceTransaction

class FinanceEntityType(DjangoObjectType):
    class Meta:
        model = FinanceEntity

class FinanceTransactionType(DjangoObjectType):
    class Meta:
        model = FinanceTransaction

class Query(object):
    finance_entity = graphene.Field(FinanceEntityType,
                                    id=graphene.Int(),
                                    name=graphene.String(),
                                    e_type=graphene.String())
    all_finance_entities = graphene.List(FinanceEntityType)

    finance_transaction = graphene.Field(FinanceTransactionType,
                                         id=graphene.Int(),
                                         e_type=graphene.String())
    all_finance_transactions = graphene.List(FinanceTransactionType)

    def resolve_finance_entity(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        if id is not None:
            return FinanceEntity.objects.get(pk=id)
        if name is not None:
            return FinanceEntity.objects.get(name=name)
        return None

    def resolve_finance_transaction(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return FinanceTransaction.objects.get(pk=id)

        return None

    def resolve_all_finance_entities(self, info, **kwargs):
        return FinanceEntity.objects.all()

    def resolve_all_finance_transactions(self, info, **kwargs):
        return FinanceTransaction.objects.select_related('t_from').all()