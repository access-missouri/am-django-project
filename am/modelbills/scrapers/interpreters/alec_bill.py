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
            return element.string
        except:
            return None

    @property
    def text(self):
        try:
            elements = self.soup.find_all('p',
                                          string=re.compile("Model Legislation"))[0].find_next_siblings("p")

            return "\n".join([el.string for el in elements])
        except:
            try:
                element_first = self.soup.find_all('p',
                                              string=re.compile("WHEREAS\b|Section\b|Amend\b"))[0]
                elements = element_first.find_next_siblings("p")
                elements[0:0] = element_first

                return "\n".join([el.string for el in elements])
            except:
                return ""