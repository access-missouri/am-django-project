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
class BallotMeasure(AMUUIDModel):
    """
    A measure to be decided by the public in a contest.

    See: OCDEP 20 -- Elections:
        https://opencivicdata.readthedocs.io/en/latest/proposals/0020.html
    """

    name = models.CharField(
        max_length=300,
        help_text='Name of the measure, as referred to on the ballot.'
    )
    ballot_title = models.TextField(
        blank=True,
        help_text="The way the measure will be explained to constituents above their vote."
    )
    ballot_summary = models.TextField(
        blank=True,
        help_text="The extended summary available to constituents on election day."
    )

    def __str__(self):
        return self.name
