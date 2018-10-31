#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Organization and related models.
"""
from __future__ import unicode_literals
from general.models import AMUUIDModel
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .election import Election


@python_2_unicode_compatible
class Contest(AMUUIDModel):
    """
    Base table: An individual race or contest.

    In variance from OCDEP 20,
    this model is designed and intended to be downcast on use.

    See: OCDEP 20 -- Elections:
        https://opencivicdata.readthedocs.io/en/latest/proposals/0020.html
    """

    name = models.CharField(
        max_length=300,
        help_text='Human-friendly name of the contest or race.',
        db_index=True
    )
    election = models.ForeignKey(
        Election,
        help_text='The full slate of contests this contest is or was a part of.'
    )

    def __str__(self):
        return self.name
