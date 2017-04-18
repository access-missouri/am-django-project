#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing http://house.mo.gov/BillContent.aspx.
"""
import re
from house_scraper.scrapers import BaseScraper


class BillDetailsScraper(BaseScraper):
    """
    Request, cache and parse http://house.mo.gov/BillContent.aspx.
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
            url_path="BillContent.aspx",
            params=params,
            **kwargs
        )

    @property
    def cache_file_path(self):
        """
        Returns the full path to a cached version of the page's content.
        """
        return '{0}/{1}?bill={bill}&year={year}&code={code}'.format(
            self.cache_dir,
            self.url_path,
            **self.params
        )

    @property
    def description(self):
        """
        Return the text of the bill's description.
        """
        return self.soup.find('div', class_='BillDescription').text.strip()

    @property
    def sponsor(self):
        """
        Return the name and url for the bill's sponsor as a dict.
        """
        tag = self.soup.find(
            'a', href=re.compile(r'/member\.aspx\?district=\d+&year=\d+')
        )
        return {
            'name': tag.text.strip(),
            'url': tag['href'].strip(),
        }
