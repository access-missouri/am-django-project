# -*- coding: utf-8 -*-
"""
Access Missouri search tools - phrase to index name Q search.
"""
import re
from django.db.models import Q
import operator
from .phrasetoqseries import phrase_to_q_series

def phrase_to_index_name_q_search(phrase):
    """
    Takes a search phrase and gives you a filter Q with everything you need to find it in index name.
    :return:
    """

    # This logic was redundant.
    return phrase_to_q_series(phrase=phrase,column_name="index_name")
