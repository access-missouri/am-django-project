#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing http://house.mo.gov/billlist.aspx.
"""
import os
from scraper.interpreters import BaseScraper


class AlecListScraper(BaseScraper):

    def __init__(self, url, **kwargs):
        """
        Initialize an object for scraping the bills list page.
        """
        super(AlecListScraper, self).__init__(
            url=url,
            **kwargs
        )

    @property
    def bill_urls(self):
        """
        Return a list or URLs for Bill.aspx parsed from the billlist.aspx markup.
        """
        list_items = self.soup.find_all('ul',
                                        class_='media-list--lines')[0].find_all('li')

        # URL is in the first <a> tag of each <th> tag.
        return [li.find('a')['href'] for li in list_items]
