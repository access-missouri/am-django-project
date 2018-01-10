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
from . import managers

@python_2_unicode_compatible
class Bill(AMBaseModel):
    """
    A proposal to be consider by a legislative body.
    """
    # Model Managers
    objects = models.Manager()
    bills = managers.BillManager()

    # Model Fields
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

    def get_bill_status(self):
        bill_status_int = 0
        # 0 - Unknown, 1 - Proposed, 2 -Revision, 3 - Agreed, 4 - Sent, 5 - Veto, 6 - Law
        actions = self.actions.all().order_by("date", "order")
        for act in actions:
            if "PROPOSE" in act.description.upper() or "OFFER" in act.description.upper():
                bill_status_int = 1
            elif "FILE" in act.description.upper():
                bill_status_int = 1
            elif "COMM" in act.description.upper() or "REFER" in act.description.upper():
                bill_status_int = 2
            elif "AGREED" in act.description.upper():
                bill_status_int = 3
            elif "OVERRIDE" in act.description.upper():
                bill_status_int = 6
            elif "SIGNED" in act.description.upper():
                bill_status_int = 6
            elif "DELIVER" in act.description.upper():
                bill_status_int = 4
            elif "VETO" in act.description.upper():
                bill_status_int = 5
        return bill_status_int

    def get_bill_status_text(self):
        bill_status_int = self.get_bill_status()
        if bill_status_int == 0:
            return "Unknown"
        elif bill_status_int == 1:
            return "Proposed"
        elif bill_status_int == 2:
            return "Revision"
        elif bill_status_int == 3:
            return "Agreed"
        elif bill_status_int == 4:
            return "Sent for Signature"
        elif bill_status_int == 5:
            return "Vetoed"
        elif bill_status_int == 6:
            return "Law"
        return "Unknown"

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

        ordering = ['-legislative_session__name','-last_action_date','identifier']

        index_together = [
            ['legislative_session', 'from_organization', 'identifier'],
        ]
