#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Integration tests around House Bill List scraping.
"""

from django.test import TestCase

from scraper.interpreters import HouseBillListInterpreter


class HouseBillListInterpreterCurrentTestCase(TestCase):

    def setUp(self):
        self.interpreter = HouseBillListInterpreter()

    def test_bill_urls_list_has_items(self):
        self.assertGreater(len(self.interpreter.bill_urls), 0)

    def test_bill_urls_list_does_not_have_none(self):
        self.assertTrue(None not in self.interpreter.bill_urls)
