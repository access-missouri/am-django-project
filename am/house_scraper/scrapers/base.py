#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Base class with properties and classes common to all Scraper subclasses.
"""
import os
import re
import requests
from requests.compat import urlparse, urljoin
from bs4 import BeautifulSoup
from datetime import date
from time import sleep
from django.conf import settings


def parse_query_str(url):
    """
    Parse the query string part out of a url into key/value pairs.

    Return a dict.
    """
    query_str = urlparse(url).query
    return {i.split('=')[0]: i.split('=')[1] for i in query_str.split('&')}


def str_to_date(date_str):
    """
    Return a date object extracted from a string in MM/DD/YYYY format.
    """
    match = re.match(
        r'(?P<month>\d{,2})/(?P<day>\d{,2})/(?P<year>\d{4})',
        date_str,
    )
    date_dict = dict([(k, int(v)) for k, v in match.groupdict().items()])

    return date(date_dict['year'], date_dict['month'], date_dict['day'])


class BaseScraper(object):
    """
    Base class with properties and classes common to all Scraper subclasses.
    """

    def __init__(
        self,
        url_path=None,
        params=None,
        session=None,
        sleep_count=1,
        no_cache=False,
    ):
        """
        Initializes an object for scraping a page.
        """
        self.url_base = "http://house.mo.gov/"
        self.url_path = url_path
        self.params = params
        self.session = session
        self.sleep_count = sleep_count
        self.no_cache = no_cache
        self._response = None
        self._soup = None
        self.cache_dir = os.path.join(
            settings.BASE_DIR,
            'house_scraper',
            '.cache',
        )

    def _request(self):
        full_url = urljoin(self.url_base, self.url_path)
        # make the request through the session, if provided
        if self.session:
            self._response = self.session.get(full_url, params=self.params)
        else:
            self._response = requests.get(full_url, params=self.params)
        sleep(self.sleep_count)
        if not self.no_cache:
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

        This property should be implemented on each subclass.
        """
        raise Exception(
            "%s has not implemented .cache_file_path." % self.__class__.__name__
        )

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
            if not self.no_cache:
                content = self.read_from_cache()
            else:
                content = None
            if not content:
                content = self.response.content
            self._soup = BeautifulSoup(content, 'html5lib')

        return self._soup
