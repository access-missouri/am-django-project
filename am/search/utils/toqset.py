# -*- coding: utf-8 -*-
"""
Access Missouri search tools - request params to filter Q.
"""
import re
from django.db.models import Q
import operator

def request_params_to_q_set_query(params):
    """
    Takes the request parameters array you get from self.request.GET and turns it into a filter Q-set.
    :param params:
    :return:
    """
    for param, value in params.items():
        q_stack_full = []

        # Looks for parameters that end with "_search" - the AM idiom for searchable fields.
        if re.match('.+_search$', param):
            search_field = param.split("_search")[0]

            # Here, we go through word by word, creating a separate Q for each.
            q_stack_words = []

            for word in value.split():
                filter_dict = {}
                filter_dict["__".join([search_field, "icontains"])] = word
                q_stack_words.append(Q(**filter_dict))

            q_full = q_stack_words.pop()

            for q in q_stack_words:
                q_full &= q

            q_stack_full.append(q_full)

    return reduce(operator.and_, q_stack_full)
