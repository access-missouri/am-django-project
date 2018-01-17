#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Models related to the State of Missouri's Legislative sessions.
"""
from __future__ import unicode_literals
from django.db import models
from general.models import (
    AMBaseModel,
    Person,
)
from .bill import Bill
from django.utils.encoding import python_2_unicode_compatible
from django_react_templatetags.mixins import RepresentationMixin



@python_2_unicode_compatible
class BillVote(RepresentationMixin, AMBaseModel):
    """
    The full question context of a vote on a bill.
    """

    bill = models.ForeignKey(
        Bill,
        related_name='votes',
        help_text='Reference to the bill being voted on.',
    )
    issue = models.CharField(
        max_length=512,
        help_text='What the vote was on - as described in journal.',
    )
    yes = models.IntegerField(
        default=0
    )
    no = models.IntegerField(
        default=0
    )
    did_not_vote = models.IntegerField(
        default=0
    )
    absent = models.IntegerField(
        default=0
    )
    did_pass = models.BooleanField(
        default=False
    )
    date = models.DateField(
        help_text="Date the vote was taken."
    )

    def get_absolute_url(self):
        return '/bills/{}/votes/{}'.format(
            self.bill.id,
            self.id,
        )

    def get_passed_yes_no(self):
        return 'Yes' if self.did_pass else 'No'

    def to_react_representation(self, context={}):
        return {
            'issue': self.issue,
            'yes': self.yes,
            'no': self.no,
            'absent': self.absent,
            'date': self.date,
        }

    def __str__(self):
        return '{} on {}'.format(
            self.issue,
            self.bill,
        )

    class Meta:
        """
        Model options.
        """

        ordering = ['-date', ]


@python_2_unicode_compatible
class PersonVote(AMBaseModel):
    """
    A vote on a bill by a person.
    """

    bill_vote = models.ForeignKey(
        BillVote,
        related_name='opinions',
        help_text='Reference to the broad vote in question.',
    )
    person = models.ForeignKey(
        Person,
        related_name='votes',
        help_text='Reference to the person casting the vote.',
    )
    opinion = models.CharField(
        max_length=12,
        help_text='What the person actually voted.',
    )

    def __str__(self):
        return '{} vote of {}: {}'.format(
            self.person,
            self.bill_vote,
            self.opinion
        )

    class Meta:
        """
        Model options.
        """

        ordering = ['-bill_vote__date', ]
