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
    Membership,
    Person,
)
from .bill import Bill
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class BillTitle(AMBaseModel):
    """
    An alternate title for a Bill.
    """

    bill = models.ForeignKey(
        Bill,
        related_name='other_titles',
        help_text='Reference to the bill with the alternate title.',
    )
    title = models.TextField(
        help_text='Alternate title for the bill.',
    )
    note = models.TextField(
        help_text='A note describing the origin of the title.',
        blank=True,
    )

    def __str__(self):
        return '{0} ({1})'.format(self.title, self.bill.identifier)


@python_2_unicode_compatible
class BillAbstract(AMBaseModel):
    """
    An available abstract (sometimes called a summary) for a Bill.
    """

    bill = models.ForeignKey(
        Bill,
        related_name='abstracts',
        help_text='Reference to the bill with the abstract.',
    )
    abstract = models.TextField(
        help_text='Text of the abstract.',
    )
    note = models.TextField(
        blank=True,
        help_text='A note about the origin of the summary.',
    )

    def __str__(self):
        return '{0} abstract'.format(self.bill.identifier)


@python_2_unicode_compatible
class BillAction(AMBaseModel):
    """
    An individual action on a bill.
    """

    bill = models.ForeignKey(
        Bill,
        related_name='actions',
        help_text='Reference to the bill that was acted on.',
    )
    organization = models.ForeignKey(
        Organization,
        related_name='actions',
        help_text='Reference to the Organization that the action took place '
                  'within.',
        null=True,
    )
    description = models.TextField(
        help_text='Description of the action.',
    )
    date = models.DateField(
        help_text='Date when the action occurred.',
    )
    order = models.PositiveIntegerField(
        help_text="Order of the action in the Bill's activity history.",
    )

    class Meta:
        """
        Model options.
        """

        ordering = ['-date', '-order']

    def __str__(self):
        return '{0} action on {1}'.format(self.bill.identifier, self.date)


@python_2_unicode_compatible
class BillVersion(AMBaseModel):
    """
    A version of a Bill.
    """

    bill = models.ForeignKey(
        Bill,
        related_name='versions',
        help_text='Reference to the Bill to which the version belongs.',
    )
    lr_number = models.CharField(
        max_length=4,
        null=True,
        blank=True,
        help_text="Second part of Legislative Reference number (after '.').",
    )
    note = models.CharField(
        max_length=300,
        help_text='Note describing the version.',
    )
    date = models.DateField(
        help_text='Date when the version was published.',
    )
    url = models.URLField(
        max_length=2000,
        help_text='Official URL where the text of the version is available.',
    )

    def __str__(self):
        return '{0} version of {1}'.format(self.date, self.bill)


@python_2_unicode_compatible
class BillAmendment(AMBaseModel):
    """
    A proposed amendment to the Bill.
    """

    bill = models.ForeignKey(
        Bill,
        related_name='amendments',
        help_text='Reference to the Bill to which the amendment was proposed.',
    )
    member = models.ForeignKey(
        Membership,
        related_name='amendments',
        help_text='Reference to the member who proposed the bill amendment.',
    )
    status = models.CharField(
        max_length=300,
        help_text='Status of the bill amendment (e.g., "Distributed", '
                  '"Withdrawn").',
    )
    url = models.URLField(
        max_length=2000,
        help_text='Official URL where the text of the amendments is available.',
    )

    def __str__(self):
        return '{0} amendment to {1}'.format(self.status, self.bill)


@python_2_unicode_compatible
class BillSponsorship(AMBaseModel):
    """
    A sponsorship of Bill by a member of a legislative body.
    """

    bill = models.ForeignKey(
        Bill,
        related_name='sponsorships',
        help_text='Reference to the sponsored Bill.',
    )
    member = models.ForeignKey(
        Membership,
        related_name='bill_sponsorships',
        help_text='Reference to the membership record for who sponsored the Bill.',
        null=True,
    )
    person = models.ForeignKey(
        Person,
        related_name='bill_sponsorships',
        help_text='The person who sponsored the bill.',
    )
    primary = models.BooleanField(
        default=False,
        help_text='Indicates the member is a primary sponsor of the Bill.',
    )
    sponsored_at = models.DateField(
        null=True,
        help_text='Date and time when the member sponsored the bill.',
    )

    def __str__(self):
        return '{} sponsorship of {}'.format(
            self.person,
            self.bill,
        )

    class Meta:
        ordering = ['-sponsored_at', '-primary',]
