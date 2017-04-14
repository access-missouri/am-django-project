#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing http://senate.mo.gov/.../Bill.aspx.
"""
from senate_scraper.scrapers import BaseScraper
from datetime import datetime, date


class BillDetailsScraper(BaseScraper):
    """
    Request, cache and parse http://senate.mo.gov/.../Bill.aspx.
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
            url_path="Bill.aspx",
            params=params,
            **kwargs
        )

    @property
    def description(self):
        """
        Return the text of the bill's description.
        """
        return self.soup.find('span', id='lblBriefDesc').text.strip()

    @property
    def effective_date(self):
        """
        Return the bill's effective date as a Python DateTime.
        """
        eff_date_text = self.soup.find('span', id='lblEffDate').text.strip()
        try:
            return datetime.strptime(eff_date_text, '%B %, %Y').date()
        except ValueError:
            return None
