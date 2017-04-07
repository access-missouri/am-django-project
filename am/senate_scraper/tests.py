#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django app for scraping the Missouri House Clerk's website.
"""
from django.test import TestCase # NOQA


class BillListTest(TestCase):
    """
    Test Senate bills listing.
    """

    def test_sanity(self):
        """
        Sanity check because I'm new.
        """
        self.assertTrue(False)
