#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing house.mo.gov lists.
"""
from scraper.interpreters import BaseInterpreter
from scraper.url_helpers import house_url


class HouseBillPageContentInterpreter(BaseInterpreter):

    def __init__(self, url):
        super(HouseBillPageContentInterpreter, self).__init__(
            url=url)

