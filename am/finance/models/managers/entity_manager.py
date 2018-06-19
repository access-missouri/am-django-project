# -*- coding: utf-8 -*-
"""
Custom model manager for finance entities.
"""
from django.db import models

class EntityQuerySet(models.QuerySet):
    """
    A custom finance entity queryset designed to handle common filtering needs.
    """
    def companies(self):
        return self.filter(e_type='corp')

    def committees(self):
        return self.filter(e_type='comm')

    def people(self):
        return self.filter(e_type='person')


class FinanceEntityManager(models.Manager):
    """
    A custom finance entity model manager that's going to live under "entities."
    """
    def get_query_set(self):
        return EntityQuerySet(self.model)

    def companies(self):
        return self.get_query_set().companies()

    def committees(self):
        return self.get_query_set().committees()

    def people(self):
        return self.get_query_set().people()
