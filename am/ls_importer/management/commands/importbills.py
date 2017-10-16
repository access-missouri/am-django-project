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
            bill_description = bill_json['bill']['description']
            bill_progress_json = bill_json['bill']['progress']
            bill_session_json = bill_json['bill']['session']
            bill_history_arr = bill_json['bill']['history']

            bill_session_name = bill_session_json['session_name']
            bill_session_type_code = ''
            if "Extra" in bill_session_name:
                bill_session_type_code = 'E'
            else:
                bill_session_type_code = 'R'

            session_object, session_created = LegislativeSession.objects.get_or_create(
                name = bill_session_name,
                classification = bill_session_type_code,
            )

            bill_object, bill_created = Bill.objects.get_or_create(
                identifier=bill_number,
                legislative_session=session_object,
            )

            print session_created
            print bill_created

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
