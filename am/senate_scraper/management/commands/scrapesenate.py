#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scrape data from the Senate Clerk website and load into OCD models.
"""
from django.core.management.base import BaseCommand
from senate_scraper.scrapers import (
    BillListScraper,
    BillDetailsScraper,
    # BillActionsScraper,
    parse_query_str,
)


class Command(BaseCommand):
    """
    Scrape data from the Senate Clerk website and load into OCD models.
    """

    help = 'Scrape data from the Senate Clerk website and load into OCD models.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        list_params = {'SessionType': 'R', }
        bill_list = BillListScraper(params=list_params)

        print '%s bills' % len(bill_list.bill_urls)
        print '============================'

        for url in bill_list.bill_urls:
            params = parse_query_str(url)
            bill_details = BillDetailsScraper(params)
            # bill_actions = BillActionsScraper(params)
            print bill_details.description
            print bill_details.effective_date
            # for action in bill_actions.actions_list:
            #     print action
            print '--------------------------------'
