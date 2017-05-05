#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unittests for bill_list scraper.
"""
import os
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
    def setUp(self):
        """
        Set up test case.
        """
        sample_markup_path = os.path.join(
            settings.BASE_DIR,
            'house_scraper/tests/sample_markup/BillContent.aspx?code=R&bill=HB1&year=2017' # noqa
        )
        with open(sample_markup_path, 'rb') as f:
            content = f.read()

        # Mock any GET request
        adapter = requests_mock.Adapter()
        adapter.register_uri('GET', requests_mock.ANY, content=content)
        with requests.Session() as session:
            session.mount('http://house.mo.gov', adapter)
            self.bill_details = BillDetailsScraper(
                {
                    'code': 'R',
                    'bill': 'HB1',
                    'year': 2017
                },
                session=session,
            )

    def test_bill_description(self):
        """
        Confirm extraction of sponsor's name.
        """
        self.assertEquals(
            self.bill_details.description,
            "Appropriates money to the Board of Fund Commissioners",
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
