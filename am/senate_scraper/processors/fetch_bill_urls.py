#!/usr/bin/env python
# -*- coding: utf-8 -*-

from legislative.models import LegislativeSession
from senate_scraper.scrapers import BillListScraper

def fetch_bill_urls(session):
    """
    Return a list of bill urls to scrape further, based on input session.
    """

    url_params = {
        'SessionType': session.web_session_type_code,
    }

    bill_list = BillListScraper(params=url_params)

    return bill_list.bill_urls
