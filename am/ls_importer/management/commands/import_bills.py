#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Import a folder (~/bills) full of bill JSON from Legiscan to the database.
"""
from django.core.management.base import BaseCommand
from legislative.models import Bill, LegislativeSession, BillAction, BillSponsorship, BodyMembership, BillText
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
            bill_text_arr = bill_json['bill']['texts']
            bill_origin_chamber = bill_json['bill']['body']
            bill_current_chamber = bill_json['bill']['current_body']

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

            for text in bill_text_arr:
                item_date = (datetime
                             .strptime(text['date'], "%Y-%m-%d")
                             .date())
                text, text_created = BillText.objects.get_or_create(
                    bill=bill_object,
                    type=text['mime'],
                    date=item_date,
                    state_url=text['state_link'],
                    ls_doc_id=text['doc_id']
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

                if bill_origin_chamber == bill_current_chamber:
                    if (bill_origin_chamber == 'H') | (bill_origin_chamber == 'S'):
                        person_body_membership, p_bod_mem_created = BodyMembership.objects.get_or_create(
                            person=person,
                            body=bill_origin_chamber,
                            session=session_object,
                        )

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
