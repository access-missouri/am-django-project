#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing house.mo.gov lists.
"""
from scraper.interpreters import BaseInterpreter


class HouseBillPageInterpreter(BaseInterpreter):

    def __init__(self, url):
        super(HouseBillPageInterpreter, self).__init__(
            url=url)

