#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Model manager for the Bill model.
"""
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

class BillManager(models.Manager):
    """
    Model manager for the Bill model.
    """
    def get_queryset(self):
        return super(BillManager, self).get_queryset()
