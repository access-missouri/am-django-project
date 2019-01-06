#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scraper for requesting, caching and parsing house.mo.gov lists.
"""
from datetime import datetime

from scraper.interpreters import BaseInterpreter


class HouseBillPageActionsInterpreter(BaseInterpreter):

    def __init__(self, url):
        self._action_table = None
        self._t_body = None
        self._actions = None
        super(HouseBillPageActionsInterpreter, self).__init__(
            url=url)

    @property
    def action_table(self):
        if not self._action_table:
            self._action_table = (self.soup
                                  .find('table', id='actionTable'))

        return self._action_table

    @property
    def actions(self):
        if not self._actions:
            actions_arr = []
            if not self._t_body:
                self._t_body = self.action_table.find("tbody")

            for row in self._t_body.find_all("tr"):
                cols = row.find_all("td")
                actions_arr.append({
                    "dateString": cols[0].get_text(),
                    "date": (datetime.strptime(
                        cols[0].get_text(),
                        "%m/%d/%Y"
                    ).date()),
                    "jrnPgString": cols[1].get_text(),
                    "description": cols[2].get_text(),
                })
            self._actions = actions_arr

        return self._actions
