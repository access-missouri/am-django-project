#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unittests for search helper utilities.
"""

from unittest import TestCase
from search.utils import *
from django.db.models import Q

class PhraseQSeriesTestCase(TestCase):
    def setUp(self):
        return

    def test_output_q_series_is_q(self):
        output_q_series = phrase_to_q_series(column_name="example", phrase="this is a test")
        self.assertIsInstance(output_q_series, Q)

    def test_output_q_series_returns_none_on_blank(self):
        output_q_series = phrase_to_q_series(column_name="example", phrase="")
        self.assertEqual(output_q_series, None)

    def test_output_q_series_is_correct(self):
        output_q_series = phrase_to_q_series(column_name="example", phrase="Alfred moose")
        independent_q_series = Q(example__icontains="Alfred")
        independent_q_series &= Q(example__icontains="moose")
        self.assertEqual(str(independent_q_series), str(output_q_series))

class PhraseIndexNameQSeriesTestCase(TestCase):
    def setUp(self):
        return

    def test_output_q_series_is_q(self):
        output_q_series = phrase_to_index_name_q_search(phrase="John W Smith")
        self.assertIsInstance(output_q_series, Q)

    def test_output_q_series_returns_none_on_blank(self):
        output_q_series = phrase_to_index_name_q_search(phrase="")
        self.assertEqual(output_q_series, None)

    def test_output_q_series_is_correct(self):
        output_q_series = phrase_to_index_name_q_search(phrase="John W Smith")
        independent_q_series = Q(index_name__icontains="John")
        independent_q_series &= Q(index_name__icontains="W")
        independent_q_series &= Q(index_name__icontains="Smith")
        self.assertEqual(str(independent_q_series), str(output_q_series))
