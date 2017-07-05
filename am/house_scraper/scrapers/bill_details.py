#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing http://house.mo.gov/BillContent.aspx.
"""
import re
from house_scraper.scrapers import BaseScraper, str_to_date


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

    @property
    def proposed_effective_date(self):
        """
        Return the Bill's proposed effective date.
        """
        tag = self.soup.find(
            'th', text='Proposed Effective Date:'
        ).find_next_sibling('td')

        return str_to_date(tag.text)

    @property
    def lr_number(self):
        """
        Return the Bill's LR Number.
        """
        tag = self.soup.find(
            'th', text='LR Number:'
        ).find_next_sibling('td')

        return tag.text.strip()

    @property
    def last_action(self):
        """
        Return a dict of last action info, including keys for date and description.
        """
        tag = self.soup.find(
            'th', text='Last Action:'
        ).find_next_sibling('td')

        split_text = tag.text.split(' - ')

        return {
            'date': str_to_date(split_text[0]),
            'description': split_text[1].strip(),
        }

    @property
    def calendar_position(self):
        """
        Return a string describing where the bill is on the legislative calendar.
        """
        tag = self.soup.find(
            'th', text='Calendar:'
        ).find_next_sibling('td')

        return tag.text.strip()
