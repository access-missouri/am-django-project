#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing http://house.mo.gov/billlist.aspx.
"""
import os
from scraper.interpreters import BaseInterpreter


class HouseBillListInterpreter(BaseInterpreter):
    """
    Request, cache and parse http://house.mo.gov/billlist.aspx.
    """

    def __init__(self, **kwargs):
        """
        Initialize an object for scraping the bills list page.
        """
        super(HouseBillListInterpreter, self).__init__(
            url='http://house.mo.gov/billlist.aspx',
            **kwargs
        )

    @property
    def bill_urls(self):
        """
        Return a list or URLs for Bill.aspx parsed from the billlist.aspx markup.
        """
        ths = (self.soup
               .find('table', id='reportgrid')
               .find_all('tr', class_='reportbillinfo'))

        urls = []

        for row in ths:
            try:
                urls.append(row.find('a')['href'])
            except TypeError:
                urls.append(None)

        # Remove the nonetypes from the empty table rows
        return filter(lambda item: item is not None, urls)
