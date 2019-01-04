#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Organization and related models.
"""
from __future__ import unicode_literals
from general.models import AMUUIDModel
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .Race import Race
from .RaceCandidate import RaceCandidate

@python_2_unicode_compatible
class RaceDivision(AMUUIDModel):
    """
    Linking table: An individual division for an individual race.

    """

    race = models.ForeignKey(
        Race,
        related_name="divisions",
        related_query_name="division",
        help_text="Where does this option appear on the ballot?"
    )
    precincts_reporting = models.IntegerField(
        default=0
    )
    precincts_total = models.IntegerField()

    def __str__(self):
        return self.id


@python_2_unicode_compatible
class RaceDivisionCandidate(AMUUIDModel):
    """
    Linking table: An individual candidates individual race results
    in an individual division.

    """
    division = models.ForeignKey(
        RaceDivision,
        related_name="candidates",
        related_query_name="candidate"
    )
    candidate = models.ForeignKey(
        RaceCandidate,
        related_name="division_candidacies",
        related_query_name="division_candidacy"
    )

    def __str__(self):
        return "{} in {}".format(self.candidate, self.division)