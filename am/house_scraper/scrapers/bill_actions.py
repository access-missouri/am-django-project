#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing http://house.mo.gov/BillActionsPrn.aspx.
"""
from house_scraper.scrapers import BaseScraper


class BillActionsScraper(BaseScraper):
    """
    Request, cache and parse http://house.mo.gov/BillActionsPrn.aspx.
    """

    def __init__(self, params, **kwargs):
        """
        Initialize an object for scraping a bill's actions page.

        Args:
            params (dict): Key/values sent in the query string when requesting
                the bill's actions.
            **kwargs: Arbitrary keyword arguments.
        """
        super(BillActionsScraper, self).__init__(
            url_path="BillActionsPrn.aspx",
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
    def actions_list(self):
        """
        Return the list of actions on the bill.
        """
        trs = self.soup.find('table', id='actionTable').find('tbody').find_all('tr')

        actions = []

        for tr in trs:
            action = {
                'date': tr.find_all('td')[0].text,
                'journal_page': tr.find_all('td')[1].text.strip(),
                'description': tr.find_all('td')[2].text.strip(),
            }
            if tr.find_all('td')[1].find('a'):
                action['journal_url'] = tr.find_all('td')[1].find('a')['href']
            else:
                action['journal_url'] = None
            actions.append(action)

        return actions
