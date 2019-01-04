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
from .Race import Race
from general.models import Person, Organization

@python_2_unicode_compatible
class RaceCandidate(AMUUIDModel):
    """
    Linking table: An individual option on the ballot.

    """

    name = models.CharField(
        max_length=300,
        help_text='Human-friendly name of the candidate or option.',
        db_index=True
    )
    race = models.ForeignKey(
        Race,
        related_name="candidates",
        related_query_name="candidate",
        help_text="Where does this option appear on the ballot?"
    )
    person = models.ForeignKey(
        Person,
        related_name="candidacies",
        related_query_name="candidacy",
        help_text="Person associated with candidacy.",
        null=True,
        blank=True
    )
    votes = models.IntegerField(
        null=True,
        blank=True
    )
    party = models.ForeignKey(
        Organization,
        null=True,
        blank=True,
        related_name="race_candidates",
        related_query_name="race_candidate"
    )

    def __str__(self):
        return self.name
