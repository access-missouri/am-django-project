#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unit tests around house URL format helper.
"""

from django.test import TestCase

from scraper.url_helpers import house_url


class HouseURLHelperUnitTestCase(TestCase):

    def test_house_url_helper_appends_without_slash(self):
        self.assertEqual(house_url("moose"), "https://house.mo.gov/moose")

    def test_house_url_helper_appends_with_slash(self):
        self.assertEqual(house_url("/moose"), "https://house.mo.gov/moose")

    def test_house_url_helper_does_nothing_if_url_complete(self):
        self.assertEqual(house_url("https://house.mo.gov/moose"), "https://house.mo.gov/moose")

    def test_house_url_helper_replaces_insecure(self):
        self.assertEqual(house_url("http://house.mo.gov/moose"), "https://house.mo.gov/moose")