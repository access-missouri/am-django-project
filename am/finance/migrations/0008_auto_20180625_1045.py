# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-25 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_auto_20180509_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meclink',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mec_links', to='finance.FinanceEntity'),
        ),
    ]
