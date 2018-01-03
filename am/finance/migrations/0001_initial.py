# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-18 21:21
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general', '0003_auto_20170804_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text=b'Date and time when the object was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text=b'Date and time when the object was last updated.')),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text=b'Key-value store suitable for storing arbitrary information not covered elsewhere.')),
                ('mec_id', models.CharField(help_text='Missouri Ethics Commission ID number.', max_length=128)),
                ('name', models.CharField(help_text='Readable name if Company or Committee.', max_length=300)),
                ('type', models.CharField(choices=[('corp', 'Company'), ('comm', 'Committee'), ('person', 'Person')], help_text='Company, Committee, or Person?', max_length=8)),
                ('first_name', models.CharField(blank=True, help_text='First name, if person.', max_length=75, null=True)),
                ('last_name', models.CharField(blank=True, help_text='First name, if person.', max_length=75, null=True)),
                ('address_first', models.CharField(blank=True, max_length=150, null=True)),
                ('address_second', models.CharField(blank=True, max_length=150, null=True)),
                ('address_city', models.CharField(blank=True, max_length=150, null=True)),
                ('address_state', models.CharField(blank=True, max_length=3, null=True)),
                ('address_zip', models.CharField(blank=True, max_length=10, null=True)),
                ('employer', models.CharField(blank=True, help_text='Employer, if person.', max_length=150, null=True)),
                ('linked_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='finance_entities', to='general.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FinanceTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text=b'Date and time when the object was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text=b'Date and time when the object was last updated.')),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text=b'Key-value store suitable for storing arbitrary information not covered elsewhere.')),
                ('type', models.CharField(choices=[('M', 'Monetary'), ('I', 'In-Kind')], max_length=1)),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
                ('t_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spending', to='finance.FinanceEntity')),
                ('t_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income', to='finance.FinanceEntity')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]