#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scrape data from the Senate Clerk website and load into OCD models.
"""
from django.core.management.base import BaseCommand
from senate_scraper.scrapers import (
    BillListScraper,
    BillDetailsScraper,
    parse_query_str,
)
from legislative.models import Bill, LegislativeSession
from general.models import Organization


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

        session = LegislativeSession.objects.get(id=1)
        senate = Organization.objects.get(id=1)

        for url in bill_list.bill_urls:
            print(url)
            params = parse_query_str(url)
            print(params)
            bill_details = BillDetailsScraper(params)
            # bill_actions = BillActionsScraper(params)

            bill, created = Bill.objects.get_or_create(
                legislative_session=session,
                identifier=params['BillID'],
                from_organization=senate,
                defaults={
                    'title': bill_details.summary,
                },
            )

            print(created)
