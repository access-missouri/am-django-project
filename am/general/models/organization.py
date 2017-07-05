#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Organization and related models.
"""
from __future__ import unicode_literals
from datetime import datetime
from general.models import AMBaseModel
from django.db import models
from django.db.models import Q
from django.utils.encoding import python_2_unicode_compatible
from general.models import Person


@python_2_unicode_compatible
class Organization(AMBaseModel):
    """
    A group of people, typically in a legislative or rule-making context.
    """

    name = models.CharField(
        max_length=300,
        help_text='Name of the Organization.',
    )
    parent = models.ForeignKey(
        'self',
        related_name='children',
        null=True,
        blank=True,
        db_index=True,
        help_text='Parent Organization of the Organization.',
    )
    ORGANIZATION_CLASSIFICATION_CHOICES = (
        ('legislature', 'Legislature'),
        ('executive', 'Executive'),
        ('party', 'Party'),
        ('committee', 'Committee'),
        ('commission', 'Commission'),
        ('corporation', 'Corporation'),
        ('agency', 'Agency'),
        ('department', 'Department'),
    )
    classification = models.CharField(
        max_length=100,
        blank=True,
        db_index=True,
        choices=ORGANIZATION_CLASSIFICATION_CHOICES,
        help_text='Categorizies the Organization',
    )

    def __str__(self):
        return self.name

    def get_parents(self):
        """
        Return all "ancestors" of the Organization.
        """
        org = self
        while True:
            org = org.parent
            # Django accesses parents lazily, so have to check if one actually exists
            if org:
                yield org
            else:
                break

    def get_current_members(self):
        """
        Return all Person objects with current memberships to the Organization.
        """
        today = datetime.date.today().isoformat()

        return Person.objects.filter(Q(memberships__start_date='') |
                                     Q(memberships__start_date__lte=today),
                                     Q(memberships__end_date='') |
                                     Q(memberships__end_date__gte=today),
                                     memberships__organization_id=self.id
                                     )


@python_2_unicode_compatible
class Post(AMBaseModel):
    """
    A position in an Organization that exists independently of the Person holding it.
    """

    label = models.CharField(
        max_length=300,
        help_text='A label describing the Post (e.g., State Senate 10).',
    )
    role = models.CharField(
        max_length=300,
        blank=True,
        help_text='The function the holder of the Post fulfills (e.g., '
                  'Senator).',
    )
    organization = models.ForeignKey(
        Organization,
        related_name='posts',
        help_text='References the Organization in which the Post exists.',
    )
    district_number = models.IntegerField(
        null=True,
        help_text='Number identifying the political district represented by the '
                  'Post.',
    )

    class Meta:
        """
        Model options.
        """

        index_together = [
            ['organization', 'label']
        ]

    def __str__(self):
        return '{} - {}'.format(self.label, self.organization)


@python_2_unicode_compatible
class Membership(AMBaseModel):
    """
    A relationship between a Person and an Organization, possibly including a Post.
    """

    organization = models.ForeignKey(
        Organization,
        related_name='memberships',
        help_text='References the Organization in which the Person is a member.',
    )
    person = models.ForeignKey(
        Person,
        related_name='memberships',
        help_text='References the Person who is a member in the Organization.',
    )
    post = models.ForeignKey(
        Post,
        related_name='memberships',
        null=True,
        help_text='References to the Post held by the member, if applicable.',
    )
    start_date = models.DateField(
        max_length=10,
        null=True,
        help_text="Date the Person's membership in the Organization starts.",
    )
    end_date = models.DateField(
        max_length=10,
        null=True,
        help_text="Date the Person's membership in the Organization ends.",
    )

    class Meta:
        """
        Model options.
        """

        index_together = [
            ['organization', 'person', 'post']
        ]

    def __str__(self):
        return '{} in {}'.format(self.person, self.organization)
