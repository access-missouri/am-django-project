#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scrape data from the House Clerk website and load into OCD models.
"""
import requests
from django.core.management.base import BaseCommand
from house_scraper.scrapers import (
    BillListScraper,
    BillDetailsScraper,
    BillActionsScraper,
    parse_query_str,
)


class Command(BaseCommand):
    """
    Scrape data from the House Clerk website and load into OCD models.
    """

    help = 'Scrape data from the House Clerk website and load into OCD models.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        with requests.Session() as session:
            bill_list = BillListScraper(session=session)

            print('%s bills' % len(bill_list.bill_urls))
            print('============================')

            for url in bill_list.bill_urls:
                params = parse_query_str(url)
                bill_details = BillDetailsScraper(params, session=session)
                bill_actions = BillActionsScraper(params, session=session)
                print('{bill} ({year}{code})'.format(**bill_details.params))
                print(bill_details.response.url)
                print(bill_details.description)
                print(bill_details.sponsor['name'])
                print(bill_details.sponsor['url'])
                for action in bill_actions.actions_list:
                    print(action)
                print('--------------------------------')
