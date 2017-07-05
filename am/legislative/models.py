#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Models related to the State of Missouri's Legislative Branch.
"""
from __future__ import unicode_literals
from django.db import models
from general.models import (
    AMBaseModel,
    Organization,
    Membership,
)
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class LegislativeSession(AMBaseModel):
    """
    A session of the Misssouri State Legislature.
    """

    name = models.CharField(
        max_length=300,
        help_text='Full official name for the Legislative Session.',
    )
    SESSION_CLASSIFICATION_CHOICES = (
        ('E', 'Extraordinary'),
        ('R', 'Regular'),
    )
    classification = models.CharField(
        max_length=100,
        choices=SESSION_CLASSIFICATION_CHOICES,
        help_text='Classifies the Legislative Session (e.g., "Regular" or '
                  '"Extraordinary").',
    )
    start_date = models.DateField(
        help_text='Date that the Legislative Session starts.',
    )
    end_date = models.DateField(
        null=True,
        help_text='Date that the Legislative Session ends, if known.',
    )
    web_session_type_code = models.CharField(
        null=True,
        blank=True,
        help_text='Used by scraper - type code for params.',
        max_length=12,
    )

    def __str__(self):
        return self.name


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
        help_text="Identifier for the bill, as assigned by the Clerk's office.",
    )
    from_organization = models.ForeignKey(
        Organization,
        related_name='bills',
        help_text='Reference to the Organization (typically a legislative '
                  'chamber) wherein the bill originated.',
    )
    title = models.TextField(
        help_text='The current title of the bill.',
    )
    lr_number = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Legislative Research (?) number.',
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

    def __str__(self):
        return '{} in {}'.format(self.identifier, self.legislative_session)

    class Meta:
        """
        Model options.
        """

        index_together = [
            ['legislative_session', 'from_organization', 'identifier'],
        ]


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

        ordering = ['order']

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
        help_text='Reference to the member who sponsored the Bill.',
    )
    primary = models.BooleanField(
        default=False,
        help_text='Indicates the member is a primary sponsor of the Bill.',
    )
    sponsored_at = models.DateTimeField(
        null=True,
        help_text='Date and time when the member sponsored the bill.',
    )

    def __str__(self):
        return '{} sponsorship of {}'.format(
            self.member.person,
            self.bill,
        )
