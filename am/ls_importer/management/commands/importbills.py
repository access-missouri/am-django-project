#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Import a folder full of bill JSON from Legiscan to the database.
"""
from django.core.management.base import BaseCommand
from senate_scraper.scrapers import (
    BillListScraper,
    BillDetailsScraper,
    parse_query_str,
)
from legislative.models import Bill, LegislativeSession
from general.models import Organization
import json


class Command(BaseCommand):
    """
    Import a folder full of bill JSON from Legiscan to the database.
    """

    help = 'Import a folder full of bill JSON from Legiscan to the database.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """

        def json_to_bill(json_path):
            json_data = open(json_path)
            bill_json = json.load(json_data)

            bill_number = bill_json['bill']['bill_number']
            bill_title = bill_json['bill']['title']
            bill_progress = bill_json['bill']['progress']
            bill_session_json = bill_json['bill']['session']


            print bill_json['bill'].viewkeys()

            print bill_session_json

        json_to_bill('/Users/nathanlawrence/Desktop/HB1.json')

        # list_params = {'SessionType': 'R', }
        # bill_list = BillListScraper(params=list_params)
        #
        # session = LegislativeSession.objects.get(id=1)
        # senate = Organization.objects.get(id=1)
        #
        # for url in bill_list.bill_urls:
        #     print(url)
        #     params = parse_query_str(url)
        #     print(params)
        #     bill_details = BillDetailsScraper(params)
        #     # bill_actions = BillActionsScraper(params)
        #
        #     bill, created = Bill.objects.get_or_create(
        #         legislative_session=session,
        #         identifier=params['BillID'],
        #         from_organization=senate,
        #         defaults={
        #             'title': bill_details.summary,
        #         },
        #     )
        #
        #     print(created)
