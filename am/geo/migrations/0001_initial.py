# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-04 16:08
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text=b'Date and time when the object was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text=b'Date and time when the object was last updated.')),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text=b'Key-value store suitable for storing arbitrary information not covered elsewhere.')),
                ('name', models.CharField(help_text='Name of the district, as shown in Access Missouri.', max_length=300)),
                ('ocd_division_id', models.CharField(help_text="Open Civic Data's unique area boundary identifier.", max_length=300)),
                ('chamber', models.CharField(blank=True, help_text='H, S, etc...', max_length=3)),
                ('bbox_top_lat', models.FloatField(blank=True, null=True)),
                ('bbox_bottom_lat', models.FloatField(blank=True, null=True)),
                ('bbox_left_lon', models.FloatField(blank=True, null=True)),
                ('bbox_right_lon', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]