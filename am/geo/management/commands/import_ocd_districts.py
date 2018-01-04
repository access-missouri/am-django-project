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

        # for person in tqdm(
        #         iterable=qset,
        #         total=qset.count()):
        #     person.index_name = person.get_full_name()
        #     person.save()
