#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Helper functions for configuring scraper URLs.
"""

def house_url(path):
    """
    Joins relative house url paths with stem or returns url if stem present.
    :param path: String path to format.
    :return: Full house URL.
    """
    stem = "https://house.mo.gov"
    # Replace insecure with secure
    if "http://" in path:
        path = path.replace("http://", "https://")
    # If the path is a full URL, just return it.
    if stem in path:
        return path
    # Reformat with or without slashes as necessary.
    if path[0] == "/":
        return "{}{}".format(stem, path)
    return "{}/{}".format(stem, path)
