# -*- coding: utf-8 -*-
"""
Access Missouri search tools - phrase to Q series.
"""
import re
from django.db.models import Q
import operator

def phrase_to_q_series(phrase,column_name):
    """
    Takes a search phrase and gives you a filter Q series with your column name.
    :return:
    """

    q_stack_words = []


    # Use spaces to split phrase into an array of words
    phrase_arr = phrase.split()

    # If the array is empty, return a Nonetype.
    if len(phrase_arr) < 1:
        return None

    # Iterate through the array, making Q objects of
    # "icontains" filters for each one.
    for word in phrase.split():
        filter_dict = {}
        filter_dict["__".join([column_name, "icontains"])] = word
        q_stack_words.append(Q(**filter_dict))

    # Now, we combine them into one Q object.
    # We start by pulling the first out of the array.
    q_full = q_stack_words.pop(0)
    # Then we iterate through the rest, combining them with a logical AND.
    for q in q_stack_words:
        q_full &= q

    return q_full
