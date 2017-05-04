#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Abstract base models which other Access Missouri models subclass.
"""
from django.db import models
from django.contrib.postgres.fields import JSONField


class AMBaseModel(models.Model):
    """
    Abstract, base model with properties shared by all Access Missouri models.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Date and time when the object was created.',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text='Date and time when the object was last updated.',
    )
    extras = JSONField(
        default=dict,
        blank=True,
        help_text='Key-value store suitable for storing arbitrary information '
                  'not covered elsewhere.',
    )

    class Meta:
        """
        Model options.
        """

        abstract = True
