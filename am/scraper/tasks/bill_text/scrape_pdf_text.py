#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AWS Lambda task for scraping a single BillText from PDF.
"""
from zappa.async import task_sns

@task_sns
def scrape_pdf_text(text_url):
    raise ValueError(text_url)