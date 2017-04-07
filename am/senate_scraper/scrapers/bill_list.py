#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing http://senate.mo.gov/17info/BTS_Web/BillList.aspx.
"""
from senate_scraper.scrapers import BaseScraper


class BillListScraper(BaseScraper):
    """
    Request, cache and parse http://senate.mo.gov/17info/BTS_Web/BillList.aspx.
    """

    def __init__(self, params, **kwargs):
        """
        Initialize an object for scraping the bills list page.
        """
        super(BillListScraper, self).__init__(
            url_path='/17info/BTS_Web/BillList.aspx',
            params=params,
            **kwargs
        )

    @property
    def bill_urls(self):
        """
        Return a list of URLs for Bill.aspx parsed from the BillList.aspx markup.
        """

        # On the senate site, these are mysteriously tucked inside tables in tables with the id "Table2"
        table_twos = self.soup.findAll('table', id='Table2')

        # URL is in the first <a> tag of each table.
        return [table_two.find('a')['href'] for table_two in table_twos]
