#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Imports district bounding boxes from the Open Civic Data API.
"""
import json
from os import getenv
from time import sleep

import requests
from django.core.management.base import BaseCommand
from tqdm import tqdm

from geo.models import District


class Command(BaseCommand):
    """
    Imports district bounding boxes from the Open Civic Data API.
    """

    help = 'Imports districts from the Open Civic Data API.'

    def handle(self, *args, **options):
        """
        Imports district bounding boxes from the Open Civic Data API.
        """

        q_set = District.objects.filter(bbox_top_lat=None)

        for dist in tqdm(
                iterable=q_set.all(),
                total=q_set.count()):

            api_url = "https://openstates.org/api/v1/districts/boundary/{}?apikey={}".format(
                dist.ocd_boundary_id,
                getenv("OCD_API_KEY"))

            response = requests.get(api_url)
            resp_json = json.loads(response.content)
            bbox = resp_json["bbox"]

            dist.bbox_left_lon = bbox[0][0]
            dist.bbox_top_lat = bbox[0][1]
            dist.bbox_right_lon = bbox[1][0]
            dist.bbox_bottom_lat = bbox[1][1]
            dist.save()

            # It's only polite!

            sleep(1)
