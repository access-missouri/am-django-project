#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Configuration of the `senate_scraper` Django app.
"""
from __future__ import unicode_literals
from django.apps import AppConfig


class SenateScraperConfig(AppConfig):
    """
    Configuration of the `senate_scraper` Django app.
    """

    name = 'senate_scraper'
    verbose_name = "Senate Clerk website scraper"
