# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-16 21:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('legislative', '0005_auto_20171016_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='from_organization',
            field=models.ForeignKey(help_text='Reference to the Organization (typically a legislative chamber) wherein the bill originated.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='general.Organization'),
        ),
    ]
