#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Scrapes bill text available in PDF.
"""
from django.core.management.base import BaseCommand
from legislative.models import BillText
from tqdm import tqdm
import requests
import re
from time import sleep
import PyPDF2
import pdfquery

class Command(BaseCommand):
    """
    Scrapes bill text available in html.
    """

    help = 'Scrapes bill text available in PDF.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """

        def ingest_bill_text(bill_text):
            result = requests.get(bill_text.state_url)
            c = result.content

            pdf_path = "scrape_cache/b_txt_{}.pdf".format(bill_text.id)

            tag_regex = re.compile("<.+?>")
            sep_line_num_regex = re.compile("\n\d+([\s\d]+)?\n")
            in_line_num_regex = re.compile("\n(\s+)?\d+\s(?=.+?\n)")
            tighten_spacing_regex = re.compile("\n\n")
            second_tighten_spacing_regex = re.compile("\n\n\s+")

            with open(pdf_path, "wb") as pdf:
                pdf.write(c)

            scraper = pdfquery.PDFQuery(pdf_path)
            scraper.load()
            scraper.tree.write("{}.xml".format(pdf_path),pretty_print=True)

            with open("{}.xml".format(pdf_path), "rb") as xml:
                strn = ' '.join(xml.readlines())
                untagged = tag_regex.sub('\n', strn)
                num_fix = sep_line_num_regex.sub('\n', untagged)
                inline_num_fix = in_line_num_regex.sub('\n', num_fix)
                tightened = tighten_spacing_regex.sub('\n', inline_num_fix)
                second_tighten = second_tighten_spacing_regex.sub('\n\n', tightened)

                bill_text.text = second_tighten
                bill_text.save()

        qset = BillText.objects.filter(type='application/pdf',
                                       text=None)

        for b_text in tqdm(
                iterable=qset,
                total=qset.count()):
            ingest_bill_text(b_text)
            sleep(1)

