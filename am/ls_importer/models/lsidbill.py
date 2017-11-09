#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Organization and related models.
"""
from __future__ import unicode_literals
from datetime import datetime
from general.models import AMBaseModel
from django.db import models
from django.db.models import Q
from django.utils.encoding import python_2_unicode_compatible
from legislative.models import Bill


@python_2_unicode_compatible
class LSIDPerson(AMBaseModel):
    """
    A group of people, typically in a legislative or rule-making context.
    """

    lsid = models.CharField(
        max_length=32,
        help_text='Legiscan ID',
        unique=True,
        db_index=True,
    )
    bill = models.ForeignKey(
        Bill,
        null=False,
        blank=False,
        related_name='ls_ids',
    )

    def __str__(self):
        return self.lsid
