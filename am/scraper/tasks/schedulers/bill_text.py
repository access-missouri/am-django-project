#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Schedule AWS Lambda tasks to scrape things with Amazon SNS.
"""
from legislative.models import BillText
from scraper.tasks.bill_text import scrape_pdf_text


def scrape_pdf_bill_text():
    q_set = BillText.objects.filter(type='application/pdf',
                                    text=None)

    for b_text in q_set:
        scrape_pdf_text(b_text.state_url)
