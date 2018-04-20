#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tag and related models.
"""
from __future__ import unicode_literals
from django.db import models
from general.models import AMBaseModel
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Tag(AMBaseModel):
    """
    A category, interest, etc that will be used to help people find things.
    """
    name = models.CharField(max_length=256,
                            null=False,
                            blank=False)
    slug = models.SlugField(max_length=128,
                            null=False,
                            blank=False,
                            unique=True)

    def get_absolute_url(self):
        return '/tags/{}'.format(self.slug)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        """
        Model options.
        """

        ordering = ['slug']
