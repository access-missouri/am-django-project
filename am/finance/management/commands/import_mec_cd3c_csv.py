#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Import a folder (~/mec/cd3_c) full of MEC CSV files to the database.
"""
from django.core.management.base import BaseCommand
import os
from tqdm import tqdm
from csv import DictReader
from datetime import datetime

from finance.models import FinanceEntity, FinanceTransaction


class Command(BaseCommand):
    """
    Import a folder (~/mec/cd3_c) full of MEC CSV files to the database.
    """

    help = 'Import a folder full of MEC CSV files to the database.'

    def handle(self, *args, **options):
        """
        Make it happen.
        """

        def csv_to_db(csv_path):
            csv_data = open(csv_path)
            csv = DictReader(csv_data)

            for row in tqdm(csv, total=len(open(csv_path).readlines())):
                from_mec_id = row[" MECID"]
                from_committee_name = row["Committee Name"]

                to_comm_name = row["Committee"]
                to_addr_one = row["Address 1"]
                to_addr_two = row["Address 2"]
                to_city = row["City"]
                to_state = row["State"]
                to_zip = row["Zip"]

                t_date = (datetime
                          .strptime(row["Date"].split(" ")[0], "%m/%d/%Y")
                          .date())
                t_amount = row["Amount"]
                t_con_type = row["Contribution Type"]

                to_obj, to_created = FinanceEntity.objects.update_or_create(
                    name__iexact=to_comm_name,
                    type="comm",
                    defaults={
                        "name": to_comm_name,
                        "address_first": to_addr_one,
                        "address_second": to_addr_two,
                        "address_city": to_city,
                        "address_state": to_state,
                        "address_zip": to_zip,
                    }
                )


                fr_obj, fr_created = FinanceEntity.objects.get_or_create(
                    name__iexact=from_committee_name,
                    type="comm",
                    defaults={
                        "name": from_committee_name,
                    }
                )

                t_obj, t_created = FinanceTransaction.objects.get_or_create(
                    t_from=fr_obj,
                    t_to=to_obj,
                    type=t_con_type,
                    amount=t_amount,
                    date=t_date
                )





        target_directory = os.path.join(os.path.expanduser("~"), 'mec', 'cd3_c')
        for file in os.listdir(target_directory):
            if file.endswith(".csv"):
                print("Starting {}.".format(file))
                csv_to_db(os.path.join(target_directory, file))
                print("Finished {}.".format(file))
