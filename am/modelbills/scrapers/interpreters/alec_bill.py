#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing http://house.mo.gov/billlist.aspx.
"""
import os
import re
from scraper.interpreters import BaseScraper


class AlecBillScraper(BaseScraper):

    def __init__(self, url, **kwargs):
        """
        Initialize an object for scraping the bills list page.
        """
        super(AlecBillScraper, self).__init__(
            url=url,
            sleep_count=3,
            **kwargs
        )

    @property
    def name(self):
        header = self.soup.find_all('h2',
                                    class_='hero__title--underline-bar')[0]

        return header.string

    @property
    def summary(self):
        try:
            element = self.soup.find_all('h2',
                                     string=re.compile("Summary"))[0].find_next_siblings("p")[0]
            return element.get_text()
        except:
            return None

    @property
    def text(self):
        split_text = re.split("Model\s[\s]+\n", self.full_page_text)
        if len(split_text) <= 2:
            return split_text[-1]
        else:
            return "\n".join(split_text[1:])

    @property
    def full_page_text(self):
        elements = []
        content_elements = self.soup.find_all('div',class_="the-content")
        for ce in content_elements:
            elements = elements + ce.find_all(['p', 'li'])
        return "\n".join([el.get_text() for el in elements])
