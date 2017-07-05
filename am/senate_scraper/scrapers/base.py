#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base class with properties and classes common to all Scraper subclasses.
"""
import os
import requests
from requests.compat import urlparse, urljoin
from bs4 import BeautifulSoup
from time import sleep
from django.conf import settings


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
        Initializes an object for scraping a page.
        """
        self.sleep_count = sleep_count
        self.url_base = "http://senate.mo.gov/17info/BTS_Web/"
        self.url_path = url_path
        self.params = params
        self._response = None
        self._soup = None
        self.cache_dir = os.path.join(
            settings.BASE_DIR,
            'senate_scraper',
            '.cache',
        )

    def _request(self):
        full_url = urljoin(self.url_base, self.url_path)
        self._response = requests.get(full_url, params=self.params)
        sleep(self.sleep_count)
        self.save_to_cache(self._response.content)
        return self._response

    def save_to_cache(self, content):
        """
        Save content of response to a local cache.
        """
        os.path.exists(self.cache_dir) or os.makedirs(self.cache_dir)
        with open(self.cache_file_path, 'wb') as f:
            f.write(content)
        return

    def read_from_cache(self):
        """
        Read from local cache of response content.
        """
        if not os.path.isfile(self.cache_file_path):
            content = None
        else:
            with open(self.cache_file_path, 'rb') as f:
                content = f.read()
        return content

    @property
    def cache_file_path(self):
        """
        Returns the full path to a cached version of the page's content.
        """
        file_path = os.path.join(
            self.cache_dir,
            self.url_path,
        )
        if self.params:
            file_path += "?%s" % '&'.join(
                ['{0}={1}'.format(k, v) for k, v in self.params.items()]
            )
        return file_path

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
            content = self.read_from_cache()
            if not content:
                content = self.response.content
            self._soup = BeautifulSoup(content, 'html5lib')

        return self._soup
