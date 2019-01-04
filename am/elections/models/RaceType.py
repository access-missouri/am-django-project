#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Organization and related models.
"""
from __future__ import unicode_literals
from general.models import AMUUIDModel
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class RaceType(AMUUIDModel):
    """
    What kind of race is it, according to the XML or TXT?

    """

    name = models.CharField(
        max_length=300,
        help_text='Human-friendly name of the race type, as provided by e-data.',
        db_index=True
    )

    def __str__(self):
        return self.name
