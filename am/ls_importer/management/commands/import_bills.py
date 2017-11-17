#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Import a folder (~/bills) full of bill JSON from Legiscan to the database.
"""
from django.core.management.base import BaseCommand
from legislative.models import Bill, LegislativeSession, BillAction, BillSponsorship
from ls_importer.models import LSIDBill, LSIDPerson
import json
from datetime import datetime
import os
from tqdm import tqdm


class Command(BaseCommand):
    """
    Import a folder (~/bills) full of bill JSON from Legiscan to the database.
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
            bill_ls_id = bill_json['bill']['bill_id']
            bill_title = bill_json['bill']['title']
            bill_description = bill_json['bill']['description']
            # bill_progress_json = bill_json['bill']['progress']
            bill_session_json = bill_json['bill']['session']
            bill_history_arr = bill_json['bill']['history']
            bill_sponsors_arr = bill_json['bill']['sponsors']

            bill_session_name = bill_session_json['session_name']
            bill_session_type_code = ''
            if "Extra" in bill_session_name:
                bill_session_type_code = 'E'
            else:
                bill_session_type_code = 'R'

            session_object, session_created = (
                LegislativeSession.objects
                .get_or_create(
                    name=bill_session_name,
                    classification=bill_session_type_code,
                ))

            bill_object, bill_created = Bill.objects.get_or_create(
                identifier=bill_number,
                legislative_session=session_object,
            )

            link_object, link_created = LSIDBill.objects.get_or_create(
                lsid=bill_ls_id,
                bill=bill_object,
            )

            bill_object.title = bill_title
            if bill_title == bill_description:
                bill_object.description = ""
            else:
                bill_object.description = bill_description
            bill_object.save()

            action_order = 0
            for history_item in bill_history_arr:
                action_order += 1
                history_item_date = (datetime
                                     .strptime(history_item['date'], "%Y-%m-%d")
                                     .date())
                action, action_created = BillAction.objects.get_or_create(
                    bill=bill_object,
                    description=history_item['action'],
                    date=history_item_date,
                    defaults={
                        'order': action_order,
                    }
                )

            for sponsorship in bill_sponsors_arr:
                person = LSIDPerson.objects.get(lsid=sponsorship['people_id']).person
                try:
                    date = (datetime
                        .strptime(bill_history_arr[-1]['date'], "%Y-%m-%d")
                        .date())
                except:
                    date = None
                primary = True if sponsorship['sponsor_type_id'] == 1 else False

                sponsorship_model, sp_m_created = BillSponsorship.objects.get_or_create(
                    bill=bill_object,
                    person=person,
                    defaults={
                        'primary':primary,
                        'sponsored_at':date,
                    },
                )

        target_directory = os.path.join(os.path.expanduser("~"), 'bills')
        for file in tqdm(os.listdir(target_directory)):
            if file.endswith(".json"):
                json_to_bill(os.path.join(target_directory, file))
