# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-13 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legislative', '0007_auto_20171016_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='billaction',
            options={'ordering': ['-date', '-order']},
        ),
    ]