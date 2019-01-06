#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing house.mo.gov lists.
"""
from scraper.interpreters import BaseInterpreter, HouseBillPageContentInterpreter
from scraper.url_helpers import house_url


class HouseBillPageInterpreter(BaseInterpreter):

    def __init__(self, url):
        self._actions = None
        self._bill_content_interpreter = None
        super(HouseBillPageInterpreter, self).__init__(
            url=url)

    @property
    def bill_content_page_url(self):
        return self.get_first_url_containing("BillContent")

    @property
    def bill_content_interpreter(self):
        if not self._bill_content_interpreter:
            self._bill_content_interpreter = HouseBillPageContentInterpreter(
                house_url(self.bill_content_page_url))
        return self._bill_content_interpreter

    @property
    def attributes(self):
        return self.bill_content_interpreter.attributes

    @property
    def actions(self):
        if not self._actions:
            self._actions = self.bill_content_interpreter.actions
        return self._actions

