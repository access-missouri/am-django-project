#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Geographic models.
"""
from __future__ import unicode_literals
from general.models import AMBaseModel
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class District(AMBaseModel):
    """
    A land area, likely a voting region or representative's base.
    """

    name = models.CharField(
        max_length=300,
        help_text='Name of the district, as shown in Access Missouri.',
    )
    ocd_division_id = models.CharField(
        max_length=300,
        help_text="Open Civic Data's unique division identifier."
    )
    ocd_boundary_id = models.CharField(
        max_length=300,
        help_text="Open Civic Data's unique area boundary identifier."
    )
    chamber = models.CharField(
        max_length=3,
        help_text="H, S, etc...",
        blank=True
    )
    bbox_top_lat = models.FloatField(
        null=True,
        blank=True
    )
    bbox_bottom_lat = models.FloatField(
        null=True,
        blank=True
    )
    bbox_left_lon = models.FloatField(
        null=True,
        blank=True
    )
    bbox_right_lon = models.FloatField(
        null=True,
        blank=True
    )


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']