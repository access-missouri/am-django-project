#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Total race result history.
"""
from __future__ import unicode_literals
from general.models import AMUUIDModel
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .Race import Race
from .RaceCandidate import RaceCandidate

@python_2_unicode_compatible
class RaceResultHistory(AMUUIDModel):
    """
    Total race result history.

    """

    race = models.ForeignKey(
        Race,
        related_name="results",
        related_query_name="result_history",
        help_text="Race result is for."
    )
    precincts_reporting = models.IntegerField(
        default=0
    )
    precincts_total = models.IntegerField()

    def __str__(self):
        return str(self.race)
