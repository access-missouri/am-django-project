#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unittests for bill_list scraper.
"""
from unittest import TestCase
from house_scraper.scrapers import BillListScraper
# import sys
# if sys.version_info.major == 3 and sys.version_info.minor >= 3:
#     from unittest.mock import patch, PropertyMock
# else:
#     from mock import patch, PropertyMock, MagicMock


class BillListScraperTest(TestCase):
    """
    Test parsing of http://house.mo.gov/billlist.aspx.
    """

    @classmethod
    def setUp(self):
        """
        Set up test case.
        """
        self.bill_list = BillListScraper()
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
        Confirm that we parse out the correct number of bills.
        """
        self.assertEquals(
            len(self.bill_list.bill_urls),
            1389,
        )


# class BillListScraperBadMarkupTest(TestCase):
#     """
#     Test that an exception is raise expected tags not found in markup.
#     """
#     def test_bill_list_not_found(self):
#         """
#         Test that an exception is raised when tag containing bill urls not found.
#         """
#         with patch(
#             'house_scraper.scrapers.BillListScraper.response',
#             new_callable=PropertyMock,
#         ) as mock_response:
#             mock_response= MagicMock(content="")
#             bill_list = BillListScraper()
#             bill_list.bill_urls
#             self.assertRaises(Exception)
