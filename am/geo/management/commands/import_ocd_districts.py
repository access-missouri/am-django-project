#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Imports districts from the Open Civic Data API.
"""
from django.core.management.base import BaseCommand
from geo.models import District
from tqdm import tqdm
import requests
from time import sleep
from os import getenv
import json
from search.utils import phrase_to_index_name_q_search
from general.models import Person
from legislative.models import BodyMembership, LegislativeSession


class Command(BaseCommand):
    """
    Imports districts from the Open Civic Data API.
    """

    help = 'Imports districts from the Open Civic Data API.'

    def handle(self, *args, **options):
        """
        Imports districts from the Open Civic Data API.
        """

        api_url = "https://openstates.org/api/v1/districts/mo/?apikey={}".format(getenv("OCD_API_KEY"))

        response = requests.get(api_url)

        districts_json = json.loads(response.content)

        for d in tqdm(districts_json):
            d_name = ""
            d_chamber = ""
            if d["chamber"] == "lower":
                d_name = "Missouri House District {}".format(d["name"])
                d_chamber = "H"
            elif d["chamber"] == "upper":
                d_name = "Missouri Senate District {}".format(d["name"])
                d_chamber = "S"
            d_obj, created = District.objects.get_or_create(
                name=d_name,
                ocd_division_id=d["division_id"],
                ocd_boundary_id=d["boundary_id"],
                chamber=d_chamber
            )

            for j_legislator in d["legislators"]:
                name_q_ified = phrase_to_index_name_q_search(j_legislator["full_name"])
                possible_people =  Person.objects.filter(name_q_ified)

                if possible_people.count() == 1:
                    membership, mem_created = BodyMembership.objects.get_or_create(
                        body=d_chamber,
                        session=LegislativeSession.objects.get(
                            name__icontains="2018"
                        ),
                        person=possible_people[0],
                        district=d_obj
                    )
