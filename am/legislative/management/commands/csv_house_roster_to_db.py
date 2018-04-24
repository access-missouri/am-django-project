#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Import a single CSV ("MemberRoster.csv") to the DB.
"""
from django.core.management.base import BaseCommand
from general.models import Person
from legislative.models import BodyMembership, LegislativeSession
from geo.models import District
from search import utils
import csv
import os
from tqdm import tqdm


class Command(BaseCommand):
    """
    Import a single CSV ("MemberRoster.csv") to the DB.
    """

    help = 'Import a single CSV ("MemberRoster.csv") to the DB.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """

        target_session_id = input("Enter target session ID:")
        target_session = LegislativeSession.objects.get(
            id=int(target_session_id)
        )
        print("Importing entries to {}.".format(target_session))

        with open(os.path.join(os.path.expanduser("~"), 'csv', 'MemberRoster.csv')) as file:
            reader = csv.DictReader(file)

            total_created = 0

            for row in reader:
                try:
                    person = (Person.objects.filter(
                                utils.phrase_to_index_name_q_search(" ".join([row['FirstName'],row['LastName']]))
                                )[0])
                    district = District.objects.get(
                        name="Missouri House District {}".format(int(row['District']))
                    )
                    membership, created = BodyMembership.objects.update_or_create(
                        body="H",
                        person=person,
                        session=target_session,
                        defaults={
                            "district": district,
                        }
                    )
                    if created:
                        total_created += 1
                except:
                    pass

            print("Created {} new memberships in {}.".format(
                total_created, target_session
            ))

        # target_directory = os.path.join(os.path.expanduser("~"), 'people')
        # for file in tqdm(os.listdir(target_directory)):
        #     if file.endswith(".json"):
        #         json_to_person(os.path.join(target_directory, file))
