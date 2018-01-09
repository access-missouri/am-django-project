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
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class LegislativeSession(AMBaseModel):
    """
    A session of the Misssouri State Legislature.
    """

    name = models.CharField(
        max_length=300,
        help_text='Full official name for the Legislative Session.',
    )
    SESSION_CLASSIFICATION_CHOICES = (
        ('E', 'Extraordinary'),
        ('R', 'Regular'),
    )
    classification = models.CharField(
        max_length=100,
        choices=SESSION_CLASSIFICATION_CHOICES,
        help_text='Classifies the Legislative Session (e.g., "Regular" or '
                  '"Extraordinary").',
    )
    start_date = models.DateField(
        help_text='Date that the Legislative Session starts.',
        null=True,
    )
    end_date = models.DateField(
        null=True,
        help_text='Date that the Legislative Session ends, if known.',
    )
    web_session_type_code = models.CharField(
        null=True,
        blank=True,
        help_text='Used by scraper - type code for params.',
        max_length=12,
    )

    def get_absolute_url(self):
        return '/legislative/sessions/{}'.format(
            self.id
        )

    def __str__(self):
        return self.name
