# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-09 14:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_auto_20180509_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financetransaction',
            old_name='type',
            new_name='e_type',
        ),
    ]
