# -*- coding: utf-8 -*-
"""
Access Missouri search tools - phrase to index name Q search.
"""
import re
from django.db.models import Q
import operator

def phrase_to_index_name_q_search(phrase):
    """
    Takes a search phrase and gives you a filter Q with everything you need to find it in index name.
    :return:
    """

    q_stack_words = []

    for word in phrase.split():
        filter_dict = {}
        filter_dict["__".join(["index_name", "icontains"])] = word
        q_stack_words.append(Q(**filter_dict))

    q_full = q_stack_words.pop()

    for q in q_stack_words:
        q_full &= q

    return q_full
