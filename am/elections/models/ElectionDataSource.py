#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Data source for election updates.
"""
from __future__ import unicode_literals
from general.models import AMUUIDModel
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .Election import Election

@python_2_unicode_compatible
class ElectionDataSource(AMUUIDModel):
    """
    Data source for election updates.

    """

    election = models.ForeignKey(
        Election,
        related_name="data_sources",
        related_query_name="data_source",
        help_text="Election data source provides information for."
    )
    SOURCE_TYPE_CHOICES = (
        ('MOSECSTXML', 'Missouri Secretary of State XML'),
        ('BOONETXT', 'Boone County TXT Results'),
    )
    source_type = models.CharField(
        max_length=12,
        choices=SOURCE_TYPE_CHOICES,
        help_text="Chooses which kind of parser gets used to store data."
    )
    source_url = models.URLField(
        max_length=2048,
        help_text="URL endpoint (with protocol) for data."
    )
    pull_data_active = models.BooleanField(
        default=False
    )

    def __str__(self):
        return "{} - {}".format(self.election, self.source_url)
