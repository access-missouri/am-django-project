# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-14 16:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legislative', '0011_auto_20171117_1533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bill',
            options={'ordering': ['-legislative_session__name', 'identifier']},
        ),
        migrations.AlterModelOptions(
            name='billsponsorship',
            options={'ordering': ['-sponsored_at', '-primary']},
        ),
    ]