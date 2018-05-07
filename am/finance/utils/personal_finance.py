#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utility methods for capturing personal finance data quickly and easily.
"""
from finance.models import FinanceTransaction

def get_all_spending(person):
    return FinanceTransaction.objects.filter(
        t_from__canonical_person=person,
    )

def get_personal_spending(person):
    return FinanceTransaction.objects.filter(
        t_from__canonical_person=person,
        t_from__type='person',
    )

def get_all_income(person):
    return FinanceTransaction.objects.filter(
        t_to__canonical_person=person,
    )

def get_personal_income(person):
    return FinanceTransaction.objects.filter(
        t_to__canonical_person=person,
        t_to__type='person',
    )
