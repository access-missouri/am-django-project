# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 15:48
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_financeentity_occupation'),
    ]

    operations = [
        migrations.CreateModel(
            name='MecLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text=b'Date and time when the object was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text=b'Date and time when the object was last updated.')),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text=b'Key-value store suitable for storing arbitrary information not covered elsewhere.')),
                ('mec_id', models.CharField(help_text='Missouri Ethics Commission ID number.', max_length=128, unique=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.FinanceEntity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='financetransaction',
            options={'ordering': ['-date']},
        ),
    ]
