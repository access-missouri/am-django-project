# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-05 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislative', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='last_action_date',
            field=models.DateField(blank=True, help_text='Date when the last action on bill happened.', null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='last_action_description',
            field=models.CharField(blank=True, help_text="Description of the bill's last action.", max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='lr_number',
            field=models.CharField(blank=True, help_text='Legislative Research (?) number.', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='proposed_effective_date',
            field=models.DateField(blank=True, help_text='Proposed date when the bill, if passed, would go into effect.', null=True),
        ),
    ]
