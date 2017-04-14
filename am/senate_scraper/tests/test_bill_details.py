#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unittests for senate's bill_list scraper.
"""
from unittest import TestCase
from senate_scraper.scrapers import BillDetailsScraper


class SenateBillDetailWellFormattedTest(TestCase):
    """
    Test basic senate bill list parsing in an ideal scenario.
    """

    @classmethod
    def setUp(self):
        """
        Set up test case.
        """
        list_params = {'BillID': 57095388, 'SessionType': 'R'}
        self.bill = BillDetailsScraper(params=list_params)
        sample_markup_path = self.bill.cache_file_path.replace(
            '.cache/',
            'tests/sample_markup/'
        )
        with open(sample_markup_path, 'rb') as f:
            self.bill.save_to_cache(
                f.read()
            )

    def test_bill_description(self):
        """
        Confirm that bill descriptions are effectively parsed.
        """
        self.assertEqual(
            self.bill.description,
            u'Adopts the Compact for a Balanced Budget',
        )

    def test_bill_number(self):
        """
        Confirm that bill descriptions are effectively parsed.
        """
        self.assertEqual(
            self.bill.number,
            u'SB 13',
        )

    def test_bill_number_as_int(self):
        """
        Confirm that bill descriptions are effectively parsed.
        """
        self.assertEqual(
            self.bill.number_as_int,
            13,
        )

    def test_bill_lr_number(self):
        """
        Confirm that the bill's LR number is properly parsed.
        """
        self.assertEqual(
            self.bill.lr_number,
            u'0308S.01I',
        )

    def test_bill_committee(self):
        """
        Check that the committee name is parsed out as string.
        """
        self.assertEqual(
            self.bill.committee,
            u'Judiciary and Civil and Criminal Jurisprudence',
        )

    def test_bill_sponsors(self):
        """
        Check that we get an array of sponsor surname strings.
        """
        self.assertEqual(self.bill.sponsors,
            ['Dixon'])

    def test_bill_summary(self):
        """
        Check that the summary is parsed out as string.
        """
        self.assertIn(
            u'Once three-fourths of the states have adopted the compact',
            self.bill.summary,
        )

    def test_bill_actions_url(self):
        """
        Check that a URL for bill actions has been successfully interpreted.
        """
        self.assertEqual(
            'http://www.senate.mo.gov/17info/BTS_Web/Actions.aspx?SessionType=R&BillID=57095388',
            self.bill.actions_url)

    def test_bill_amendments_url(self):
        """
        Check that the amendments URL gets parsed.
        """
        self.assertEqual(
            'http://www.senate.mo.gov/17info/BTS_Amendments?SessionType=R&BillID=57095388',
            self.bill.amendments_url)

    def test_bill_full_text_url(self):
        """
        Check that the full text URL gets parsed.
        """
        self.assertEqual(
            'http://www.senate.mo.gov/17info/BTS_Web/BillText.aspx?SessionType=R&BillID=57095388',
            self.bill.full_text_url)

    def test_bill_committee_url(self):
        """
        Check that the committee name is parsed out as string.
        """
        self.assertEqual(
            self.bill.committee_url,
            u'http://www.senate.mo.gov/JUDI',
        )
