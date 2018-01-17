#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Finance transaction and related models.
"""
from __future__ import unicode_literals
from datetime import datetime
from general.models import AMBaseModel
from django.db import models
from . import FinanceEntity

from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class FinanceTransaction(AMBaseModel):
    """
    Someone spent money on something.
    """

    t_from = models.ForeignKey(FinanceEntity,
                               related_name="spending")
    t_to = models.ForeignKey(FinanceEntity,
                             related_name="income")
    TRANSACTION_TYPE_CHOICES = (
        ('M', 'Monetary'),
        ('I', 'In-Kind'),
    )
    type = models.CharField(
        max_length=1,
        choices=TRANSACTION_TYPE_CHOICES
    )
    date = models.DateField()
    amount = models.FloatField()

    def __str__(self):
        return "From {} to {} - {}".format(self.t_from.name, self.t_to.name, self.amount)

    def get_absolute_url(self):
        return "/finance/transactions/{}".format(self.id)

    class Meta:
        """
        Model options.
        """

        ordering = ['-date']

