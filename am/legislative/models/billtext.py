#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Models related to the State of Missouri's Legislative sessions.
"""
from __future__ import unicode_literals
from django.db import models
from general.models import (
    AMBaseModel,
)
from legislative.models import Bill
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class BillText(AMBaseModel):
    """
    The full text of a bill.
    """

    bill = models.ForeignKey(Bill,
                             related_name="text_versions")
    type = models.CharField(max_length=140)
    date = models.DateField()
    state_url = models.URLField(max_length=2000)
    ls_doc_id = models.CharField(max_length=50,
                                 blank=True,
                                 null=True)
    text = models.TextField(blank=True,
                            null=True)



    def __str__(self):
        return '{} - {}'.format(self.bill, self.date)

    class Meta:
        """
        Model options.
        """

        ordering = ['bill__identifier', '-date']
