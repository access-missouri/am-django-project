#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base class with properties and classes common to all Scraper subclasses.
"""
import requests
from requests.compat import urlparse, urljoin
from bs4 import BeautifulSoup
from time import sleep


def parse_query_str(url):
    """
    Parse the query string part out of a url into key/value pairs.

    Return a dict.
    """
    query_str = urlparse(url).query
    return {i.split('=')[0]: i.split('=')[1] for i in query_str.split('&')}


class BaseScraper(object):
    """
    Base class with properties and classes common to all Scraper subclasses.
    """

    def __init__(self, url_path=None, params=None, sleep_count=1):
        """
        Initials an object for scraping a page.
        """
        self.sleep_count = sleep_count
        self.url_base = "http://house.mo.gov/"
        self.url_path = url_path
        self.params = params
        self._response = None
        self._soup = None

    def _request(self):
        full_url = urljoin(self.url_base, self.url_path)
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
        if not self._soup:
            self._soup = BeautifulSoup(self.response.content, 'html5lib')

        return self._soup
