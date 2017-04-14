#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unittests for senate's bill_list scraper.
"""
from unittest import TestCase
from senate_scraper.scrapers import BillListScraper


class SenateBillListWellFormattedTest(TestCase):
    """
    Test basic senate bill list parsing in an ideal scenario.
    """

    @classmethod
    def setUp(self):
        """
        Set up test case.
        """
        list_params = {'SessionType': 'R', }
        self.bill_list = BillListScraper(params=list_params)
        sample_markup_path = self.bill_list.cache_file_path.replace(
            '.cache/',
            'tests/sample_markup/'
        )
        with open(sample_markup_path, 'rb') as f:
            self.bill_list.save_to_cache(
                f.read()
            )

    def test_bill_urls_count(self):
        """
        Confirm that we parse out the correct number of bills - 598 for this sample.
        """
        self.assertEquals(
            len(self.bill_list.bill_urls),
            598,
        )
