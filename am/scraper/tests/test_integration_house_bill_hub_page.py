#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Integration tests around House Bill hub page scraping.
"""

from django.test import TestCase

from scraper.interpreters import HouseBillPageInterpreter


class HouseBillHubPageInterpreterTestCase(TestCase):

    def setUp(self):
        self.interpreter = HouseBillPageInterpreter(
            url="https://raw.githubusercontent.com/access-missouri/am-scraper-test-mirror/master/house/bills/20190105-hb-26-bill-page.html") #noqa

    def test_access_attributes_dictionary(self):
        self.assertGreater(len(self.interpreter.attributes), 0)

    def test_access_actions(self):
        self.assertGreater(len(self.interpreter.actions), 0)
