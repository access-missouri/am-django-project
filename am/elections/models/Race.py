#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Organization and related models.
"""
from __future__ import unicode_literals


from general.models import AMUUIDModel
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from .Election import Election
from .RaceType import RaceType
from .ElectionDataSource import ElectionDataSource
from geo.models import District

@python_2_unicode_compatible
class Race(AMUUIDModel):
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
        related_name="races",
        related_query_name="race",
        help_text="The full slate of contests this contest is or was a part of."
    )
    jurisdiction = models.ForeignKey(
        District,
        null=True,
        blank=True,
        related_name="election_races",
        related_query_name="election_race",
        help_text="Where is this race taking place?"
    )
    race_type = models.ForeignKey(
        RaceType,
        null=True,
        blank=True,
        related_name="races",
        related_query_name="race"
    )
    data_source = models.ForeignKey(
        ElectionDataSource,
        null=True,
        blank=True,
        related_name="races",
        related_query_name="race"
    )
    data_source_race_name = models.CharField(
        max_length=1000,
        blank=True
    )
    votes_last_updated = models.DateTimeField(
        null=True,
        blank=True
    )
    precincts_reporting = models.IntegerField(
        default=0
    )
    precincts_total = models.IntegerField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
