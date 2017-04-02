#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing http://house.mo.gov/billlist.aspx.
"""
from house_scraper.scrapers import BaseScraper


class BillListScraper(BaseScraper):
    """
    Request, cache and parse http://house.mo.gov/billlist.aspx.
    """

    def __init__(self, **kwargs):
        """
        Initialize an object for scraping the bills list page.
        """
        super(BillListScraper, self).__init__(
            url_path='/billlist.aspx',
            **kwargs
        )

    @property
    def bill_urls(self):
        """
        Return a list or URLs for Bill.aspx parsed from the billlist.aspx markup.
        """
        # Get all the <th> tag in the this table.
        ths = self.soup.find('table', id='billAssignGroup').find_all('th')
        # URL is in the first <a> tag.
        return [th.find('a')['href'] for th in ths]
