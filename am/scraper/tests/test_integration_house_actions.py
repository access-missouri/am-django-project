#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Integration tests around House Bill List scraping.
"""

from datetime import datetime

from django.test import TestCase

from scraper.interpreters import HouseBillPageActionsInterpreter


class HouseBillActionsInterpreterTestCase(TestCase):

    def setUp(self):
        self.interpreter = HouseBillPageActionsInterpreter(
            url="https://raw.githubusercontent.com/access-missouri/am-scraper-test-mirror/master/house/bills/20190105-hb-26-bill-actions.html") #noqa

    def test_bill_actions_table_exists(self):
        self.assertTrue(self.interpreter.action_table is not None)

    def test_actions_list_has_items(self):
        self.assertGreater(len(self.interpreter.actions), 0)

    def test_actions_list_has_prefile_item(self):
        self.assertTrue("Prefile" in self.interpreter.actions[0]["description"])

    def test_actions_list_prefile_item_has_date_string(self):
        self.assertEqual(self.interpreter.actions[0]["dateString"], "12/03/2018")

    def test_actions_list_prefile_item_has_jrn_pg_empty(self):
        self.assertEqual(self.interpreter.actions[0]["jrnPgString"], "")

    def test_actions_list_prefile_item_has_accurate_date(self):
        self.assertEqual(self.interpreter.actions[0]["date"], (datetime.now()
                                                               .replace(2018, 12, 03)
                                                               .date()))
