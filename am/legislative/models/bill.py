#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Models related to the State of Missouri's Legislative sessions.
"""
from __future__ import unicode_literals
from django.db import models
from general.models import (
    AMBaseModel,
    Organization,
)
from .legislativesession import LegislativeSession
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Bill(AMBaseModel):
    """
    A proposal to be consider by a legislative body.
    """

    legislative_session = models.ForeignKey(
        LegislativeSession,
        related_name='bills',
        help_text='Reference to the Legislative Session in which the Bill was '
                  'considered.',
    )
    identifier = models.CharField(
        max_length=100,
        help_text="Identifier for the bill, as assigned by the Clerk's office "
                  "(e.g., 'HB1', 'SB2')."
    )
    from_organization = models.ForeignKey(
        Organization,
        related_name='bills',
        help_text='Reference to the Organization (typically a legislative '
                  'chamber) wherein the bill originated.',
        null=True,
    )
    title = models.TextField(
        help_text='The current title of the bill.',
    )
    lr_number = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        help_text="First part of Legislative Reference number (before '.').",
    )
    proposed_effective_date = models.DateField(
        null=True,
        blank=True,
        help_text='Proposed date when the bill, if passed, would go into '
                  'effect.',
    )
    last_action_date = models.DateField(
        null=True,
        blank=True,
        help_text='Date when the last action on bill happened.',
    )
    last_action_description = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        help_text="Description of the bill's last action.",
    )
    calendar_position = models.CharField(
        max_length=300,
        null=True,
        help_text='Current position of the bill on the legislative calendar.',
    )
    description = models.TextField(
        help_text="Description of the purpose of the bill.",
        blank=True,
    )

    def get_absolute_url(self):
        return '/bills/{}'.format(
            self.id,
        )

    def __str__(self):
        return '{} in {}'.format(self.identifier, self.legislative_session)

    class Meta:
        """
        Model options.
        """

        ordering = ['-legislative_session__name','identifier']

        index_together = [
            ['legislative_session', 'from_organization', 'identifier'],
        ]
