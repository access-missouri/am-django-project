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
class Election(AMUUIDModel):
    """
    An entire set of different races or contests to be held together.

    See: OCDEP 20 -- Elections:
        https://opencivicdata.readthedocs.io/en/latest/proposals/0020.html
    """

    name = models.CharField(
        max_length=300,
        help_text='Human-friendly name of the election.',
        db_index=True
    )
    election_day = models.DateField(
        blank=True,
        null=True,
        db_index=True
    )

    def __str__(self):
        return self.name
