# -*- coding: utf-8 -*-
"""
Access Missouri search tools - request params to filter dict.
"""
import re

def request_params_to_filter_dict(params):
    """
    Takes the request parameters array you get from self.request.GET and turns it into a filter dict.
    :param params:
    :return:
    """
    filter_dict = {}
    for param, value in params.items():
        # Looks for parameters that end with "_search" - the AM idiom for searchable fields.
        if re.match('.+_search$', param):
            search_field = param.split("_search")[0]
            filter_dict["__".join([search_field, "icontains"])] = value

    return filter_dict
