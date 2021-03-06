# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-14 16:08
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_auto_20170804_2100'),
        ('legislative', '0012_auto_20171214_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text=b'Date and time when the object was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text=b'Date and time when the object was last updated.')),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text=b'Key-value store suitable for storing arbitrary information not covered elsewhere.')),
                ('body', models.CharField(choices=[('H', 'House'), ('S', 'Senate'), ('E', 'Executive')], help_text='Classifies the body type (e.g., "House" or "Senate").', max_length=2)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='body_memberships', to='general.Person')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='body_memberships', to='legislative.LegislativeSession')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
