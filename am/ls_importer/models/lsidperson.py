#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
LSID-person linking class.
"""
from __future__ import unicode_literals
from general.models import AMBaseModel
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from general.models import Person


@python_2_unicode_compatible
class LSIDPerson(AMBaseModel):
    """
    Legiscan Person-ID Linking class.
    """

    lsid = models.CharField(
        max_length=32,
        help_text='Legiscan ID',
        unique=True,
        db_index=True,
    )
    person = models.ForeignKey(
        Person,
        null=False,
        blank=False,
        related_name='ls_ids',
    )

    def __str__(self):
        return self.lsid
