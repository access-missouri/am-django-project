#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scrape data from the Senate Clerk website and load into OCD models.
"""
from django.core.management.base import BaseCommand
# from senate_scraper.scrapers import (
#     BillListScraper,
#     BillDetailsScraper,
#     parse_query_str,
# )
from legislative.models import Bill
from general.models import Organization
from senate_scraper.processors import update_senate_bill

from tqdm import tqdm


class Command(BaseCommand):
    """
    Scrape data from the Senate Clerk website and load into OCD models.
    """

    help = 'Scrape data from the Senate Clerk website and load into OCD models.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        # session = LegislativeSession.objects.get(id=1)
        senate = Organization.objects.get(id=1)

        bills = Bill.objects.filter(from_organization=senate)

        for bill in tqdm(bills):
            update_senate_bill(bill=bill)
