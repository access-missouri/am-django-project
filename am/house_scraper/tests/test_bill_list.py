#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unittests for bill_list scraper.
"""
import os
import re
from django.conf import settings
from unittest import TestCase
from house_scraper.scrapers import BillListScraper
import requests
import requests_mock


class BillListScraperTest(TestCase):
    """
    Test parsing of http://house.mo.gov/billlist.aspx.
    """

    @classmethod
    @requests_mock.Mocker()
    def setUp(self, m):
        """
        Set up test case.
        """
        sample_markup_path = os.path.join(
            settings.BASE_DIR,
            'house_scraper',
            'tests/sample_markup/billlist.aspx'
        )
        with open(sample_markup_path, 'rb') as f:
            content = f.read()

        # Mock responses for requests that pass any non-empty string as a URL.
        pattern = re.compile(r'.+')
        m.get(pattern, content=content)

        self.bill_list = BillListScraper(session=requests.session())

    def test_bill_urls_count(self):
        """
        Confirm that we parse out the correct number of bills.
        """
        self.assertEquals(
            len(self.bill_list.bill_urls),
            1389,
        )


class BillListScraperBadMarkupTest(TestCase):
    """
    Test that an exception is raised when expected tags not found in markup.
    """

    @classmethod
    @requests_mock.Mocker()
    def setUp(self, m):
        """
        Set up test case.
        """
        sample_markup_path = os.path.join(
            settings.BASE_DIR,
            'house_scraper',
            'tests/sample_markup/index.aspx'
        )
        with open(sample_markup_path, 'rb') as f:
            content = f.read()

        # Mock responses for requests that pass any non-empty string as a URL.
        pattern = re.compile(r'.+')
        m.get(pattern, content=content)

        self.bill_list = BillListScraper(session=requests.session())
    
    def test_bill_list_not_found(self):
        """
        Test that an exception is raised when tag containing bill urls not found.
        """
        self.bill_list.bill_urls
        self.assertRaises(Exception)
