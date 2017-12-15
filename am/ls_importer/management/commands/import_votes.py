#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Import a folder (~/votes) full of vote JSON from Legiscan to the database.
"""
from django.core.management.base import BaseCommand
from legislative.models import BillVote, PersonVote
from ls_importer.models import LSIDPerson, LSIDBill
import json
from datetime import datetime
import os
from tqdm import tqdm


class Command(BaseCommand):
    """
    Import a folder (~/votes) full of vote JSON from Legiscan to the database.
    """

    help = 'Import a folder full of vote JSON from Legiscan to the database.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """
        def json_to_vote(json_path):
            json_data = open(json_path)
            vote_json = json.load(json_data)['roll_call']

            # vote_ls_id = vote_json['roll_call_id']
            bill_ls_id = vote_json['bill_id']
            vote_date = datetime.strptime(vote_json['date'], "%Y-%m-%d")
            vote_issue = vote_json['desc']
            vote_yes = vote_json['yea']
            vote_no = vote_json['nay']
            vote_nv = vote_json['nv']
            vote_absent = vote_json['absent']
            vote_passed = True if vote_json['passed'] > 0 else False

            vote_opinions = vote_json['votes']

            vote_bill = LSIDBill.objects.get(
                lsid=bill_ls_id
            ).bill


            broad_vote, broad_vote_created = BillVote.objects.get_or_create(
                bill=vote_bill,
                date=vote_date,
                issue=vote_issue,
                defaults={
                    'yes': vote_yes,
                    'no': vote_no,
                    'did_not_vote': vote_nv,
                    'absent': vote_absent,
                    'did_pass': vote_passed,
                }
            )

            for opinion in vote_opinions:
                person = LSIDPerson.objects.get(
                    lsid=opinion['people_id'],
                ).person

                opinion_mod, op_mod_created = PersonVote.objects.update_or_create(
                    person=person,
                    bill_vote=broad_vote,
                    opinion=opinion['vote_text'],
                )

        target_directory = os.path.join(os.path.expanduser("~"), 'votes')
        for file in tqdm(os.listdir(target_directory)):
            if file.endswith(".json"):
                json_to_vote(os.path.join(target_directory, file))
