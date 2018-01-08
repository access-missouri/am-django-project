#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing http://house.mo.gov/billlist.aspx.
"""
import os
from scraper.interpreters import BaseScraper


class BillListScraper(BaseScraper):
    """
    Request, cache and parse http://house.mo.gov/billlist.aspx.
    """

    def __init__(self, **kwargs):
        """
        Initialize an object for scraping the bills list page.
        """
        super(BillListScraper, self).__init__(
            url_path='billlist.aspx',
            **kwargs
        )

    @property
    def cache_file_path(self):
        """
        Returns the full path to a cached version of the page's content.
        """
        return os.path.join(self.cache_dir, self.url_path)

    @property
    def bill_urls(self):
        """
        Return a list or URLs for Bill.aspx parsed from the billlist.aspx markup.
        """
        ths = self.soup.find('table', id='billAssignGroup').find_all('th')

        # URL is in the first <a> tag of each <th> tag.
        return [th.find('a')['href'] for th in ths]
