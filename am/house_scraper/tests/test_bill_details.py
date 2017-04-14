#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unittests for bill_list scraper.
"""
import os
import re
from django.conf import settings
from unittest import TestCase
from house_scraper.scrapers import BillDetailsScraper
import requests
import requests_mock


class BillDetailsScraperTest(TestCase):
    """
    Test parsing of http://house.mo.gov/BillContent.aspx.
    """

    @classmethod
    @requests_mock.Mocker()
    def setUp(self, m):
        """
        Set up test case.
        """
        sample_markup_path = os.path.join(
            settings.BASE_DIR,
            'house_scraper/tests/sample_markup/BillContent.aspx?code=R&bill=HB1&year=2017' # noqa
        )
        with open(sample_markup_path, 'rb') as f:
            content = f.read()

        # Mock responses for requests that pass any non-empty string as a URL.
        pattern = re.compile(r'.+')
        m.get(pattern, content=content)

        self.bill_details = BillDetailsScraper(
            {
                'code': 'R',
                'bill': 'HB1',
                'year': 2017
            },
            session=requests.session(),
        )

    def test_bill_sponsor_name(self):
        """
        Confirm extraction of sponsor's name.
        """
        self.assertEquals(
            self.bill_details.sponsor['name'],
            "Fitzpatrick, Scott (158)",
        )

    def test_bill_sponsor_url(self):
        """
        Confirm extraction of sponsor's url.
        """
        self.assertEquals(
            self.bill_details.sponsor['url'],
            "/member.aspx?district=158&year=2017"
        )
