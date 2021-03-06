# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-05 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='parent',
            field=models.ForeignKey(blank=True, help_text='Parent Organization of the Organization.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='general.Organization'),
        ),
    ]
