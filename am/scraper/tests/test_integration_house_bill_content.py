#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Integration tests around House Bill "content" scraping.
"""

from django.test import TestCase

from scraper.interpreters import HouseBillPageContentInterpreter


class HouseBillContentInterpreterTestCase(TestCase):

    def setUp(self):
        self.interpreter = HouseBillPageContentInterpreter(
            url="https://raw.githubusercontent.com/access-missouri/am-scraper-test-mirror/master/house/bills/20190105-hb-26-bill-content.html") #noqa

    def test_attributes_dictionary_captured(self):
        self.assertEqual(len(self.interpreter.attributes), 7)

    def test_access_actions(self):
        self.assertGreater(len(self.interpreter.actions), 0)
