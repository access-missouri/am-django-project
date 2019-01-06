#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing house.mo.gov lists.
"""
from scraper.interpreters import BaseInterpreter, HouseBillPageActionsInterpreter
from scraper.url_helpers import house_url

class HouseBillPageContentInterpreter(BaseInterpreter):

    def __init__(self, url):
        self._attributes = None
        self._actions_interpreter = None
        self._actions = None
        super(HouseBillPageContentInterpreter, self).__init__(
            url=url)

    @property
    def attributes(self):
        if not self._attributes:
            attributes_rows = (self.soup
                               .find("div", id="BillJunk")
                               .find("table")
                               .find("tbody")
                               .find_all("tr"))
            attributes = {}
            for row in attributes_rows:
                # Skip over any rows that don't have labels.
                if row.find("th"):
                    attributes.update([(
                        row.find("th").get_text(),
                        row.find("td").get_text()
                    )])
            self._attributes = attributes

        return self._attributes

    @property
    def bill_actions_page_url(self):
        return self.get_first_url_containing("BillActions")

    @property
    def actions_interpreter(self):
        if not self._actions_interpreter:
            self._actions_interpreter = HouseBillPageActionsInterpreter(
                house_url(self.bill_actions_page_url))
        return self._actions_interpreter

    @property
    def actions(self):
        if not self._actions:
            self._actions = self.actions_interpreter.actions
        return self._actions
