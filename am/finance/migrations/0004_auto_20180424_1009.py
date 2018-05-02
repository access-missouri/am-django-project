# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-24 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_auto_20171221_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financeentity',
            name='mec_id',
            field=models.CharField(blank=True, help_text='Missouri Ethics Commission ID number.', max_length=128),
        ),
    ]