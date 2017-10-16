#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Person and related models.
"""
from __future__ import unicode_literals
from django.db import models
from general.models import AMBaseModel
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Person(AMBaseModel):
    """
    An individual who may have served in or been a candidate for a political office.
    """

    first_name = models.CharField(
        max_length=300,
        db_index=True,
        help_text="First name of the Person.",
    )
    middle_name = models.CharField(
        max_length=300,
        db_index=True,
        blank=True,
        help_text="Middle name (or initial) of the Person.",
    )
    last_name = models.CharField(
        max_length=300,
        db_index=True,
        help_text="Last name of the Person.",
    )
    suffix = models.CharField(
        max_length=10,
        db_index=True,
        blank=True,
        help_text="Name suffix (e.g., 'Jr.', 'Sr.', 'III') of the Person.",
    )
    nickname = models.CharField(
        max_length=300,
        db_index=True,
        blank=True,
        help_text="Last name of the Person.",
    )
    gender = models.CharField(
        max_length=100,
        blank=True,
        help_text="Gender of the Person, if known.",
    )

    def __str__(self):
        template = '{0.last_name}, {0.suffix}, {0.first_name} "{0.nickname}" {0.middle_name}' # noqa
        return (
            template.format(self)
            # remove the suffix placeholder, if empty
            .replace(', , ', ', ')
            # remove the nickname placeholder, if empty
            .replace(' ""', '')
            # remove the middle_name placeholder, if empty
            .replace('  ', '')
        )

    class Meta:
        """
        Model options.
        """

        verbose_name_plural = "people"