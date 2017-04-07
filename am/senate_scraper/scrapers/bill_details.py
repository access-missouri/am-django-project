#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing http://senate.mo.gov/BillContent.aspx.
"""
from senate_scraper.scrapers import BaseScraper


class BillDetailsScraper(BaseScraper):
    """
    Request, cache and parse http://senate.mo.gov/BillContent.aspx.
    """

    def __init__(self, params, **kwargs):
        """
        Initialize an object for scraping a bill's details page.

        Args:
            params (dict): Key/values sent in the query string when requesting
                the bill's actions.
            **kwargs: Arbitrary keyword arguments.
        """
        super(BillDetailsScraper, self).__init__(
            url_path="/BillContent.aspx",
            params=params,
            **kwargs
        )

    @property
    def description(self):
        """
        Return the text of the bill's description.
        """
        return self.soup.find('div', class_='BillDescription').text.strip()
