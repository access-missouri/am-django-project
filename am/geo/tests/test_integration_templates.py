#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Integration tests around template rendering for geo.
"""

from django.test import TestCase
from django.test import Client

class DistrictIntegrationTestCase(TestCase):
    fixtures = ['geo.json']

    def setUp(self):
        # Set up Django integrated testing request client
        self.client = Client()

    def test_district_detail_renders_without_error(self):
        response = self.client.get("/geo/districts/175/")
        self.assertEqual(response.status_code, 200)

    def test_district_detail_context_gives_correct_url(self):
        response = self.client.get("/geo/districts/175/")
        self.assertEqual(response.context["district"].get_absolute_url(), u"/geo/districts/175/")

    def test_district_detail_context_str_gives_string(self):
        response = self.client.get("/geo/districts/175/")
        self.assertIsInstance(response.context["district"].__str__(), str)

    def test_district_detail_without_slash_renders_redirect(self):
        response = self.client.get("/geo/districts/175")
        self.assertEqual(response.status_code, 301)

    def test_malformed_district_url_gives_not_found(self):
        response = self.client.get("/geo/districts/111111/")
        self.assertEqual(response.status_code, 404)

