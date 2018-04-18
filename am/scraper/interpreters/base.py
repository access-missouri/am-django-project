#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base class with properties and classes common to all Scraper subclasses.
"""
import requests
from requests.compat import urlparse, urljoin
from bs4 import BeautifulSoup
from time import sleep


class BaseScraper(object):
    """
    Base class with properties and classes common to all Scraper subclasses.
    """

    def __init__(self, url=None, sleep_count=1):
        """
        Initializes an object for scraping a page.
        """
        self.sleep_count = sleep_count
        self.url = url
        self._soup = None

    def _request(self):
        full_url = self.url
        self._response = requests.get(full_url, params=self.params)
        sleep(self.sleep_count)
        return self._response



    @property
    def response(self):
        """
        Returns the response of the page request.
        """
        if not self._response:
            self._response = self._request()

        return self._response

    @property
    def soup(self):
        """
        Return parsed response content as a BeautifulSoup object.
        """
        content = self.response.content
        self._soup = BeautifulSoup(content, 'html5lib')

        return self._soup
