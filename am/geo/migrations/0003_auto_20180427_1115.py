# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-27 16:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0002_auto_20180104_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'ordering': ['name']},
        ),
    ]