#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Models related to the State of Missouri's Legislative sessions.
"""
from __future__ import unicode_literals
from django.db import models
from general.models import (
    AMBaseModel, Person
)
from legislative.models import LegislativeSession
from django.utils.encoding import python_2_unicode_compatible
from geo.models import District

@python_2_unicode_compatible
class BodyMembership(AMBaseModel):
    """
    A person's body membership in a session of the Misssouri State Legislature.
    """

    BODY_CHOICES = (
        ('H', 'House'),
        ('S', 'Senate'),
        ('E', 'Executive'),
    )
    person = models.ForeignKey(Person,
                               related_name="body_memberships")
    body = models.CharField(
        max_length=2,
        choices=BODY_CHOICES,
        help_text='Classifies the body type (e.g., "House" or '
                  '"Senate").',
    )
    session = models.ForeignKey(LegislativeSession,
                                related_name="body_memberships")
    district = models.ForeignKey(District,
                                 null=True,
                                 blank=True)

    def __str__(self):
        return '{}({}) in {}'.format(self.person, self.body, self.session)

    def get_num_bills_sponsored(self):
        return self.bill_sponsorships.count()

    def get_num_bills_primary_sponsored(self):
        return self.bill_sponsorships.filter(primary=True).count()

    class Meta:
        """
        Model options.
        """

        ordering = ['-session__name']
