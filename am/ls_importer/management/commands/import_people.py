#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Import a folder (~/people) full of person JSON from Legiscan to the database.
"""
from django.core.management.base import BaseCommand
from general.models import Person
import json
from datetime import datetime
import os
from tqdm import tqdm


class Command(BaseCommand):
    """
    Import a folder (~/people) full of person JSON from Legiscan to the database.
    """

    help = 'Import a folder full of person JSON from Legiscan to the database.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """

        def json_to_person(json_path):
            json_data = open(json_path)
            person_json = json.load(json_data)
            pj_unfold = person_json['person']

            person_ls_id = pj_unfold['people_id']
            person_ls_role_id = pj_unfold['role_id']
            person_role = pj_unfold['role']
            person_ls_party_id = pj_unfold['party_id']
            person_name = pj_unfold['name']
            person_first_name = pj_unfold['first_name']
            person_middle_name = pj_unfold['middle_name']
            person_last_name = pj_unfold['last_name']
            person_suffix = pj_unfold['suffix']
            person_nickname = pj_unfold['nickname']


            person_object, person_created = Person.objects.get_or_create(
                first_name=person_first_name,
                middle_name=person_middle_name,
                last_name=person_last_name,
                suffix=person_suffix,
                defaults={
                    'nickname': person_nickname,
                }
            )

        target_directory = os.path.join(os.path.expanduser("~"), 'people')
        for file in tqdm(os.listdir(target_directory)):
            if file.endswith(".json"):
                json_to_person(os.path.join(target_directory, file))
