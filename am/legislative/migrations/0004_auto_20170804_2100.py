# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-04 21:00
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislative', '0003_legislativesession_web_session_type_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='description',
            field=models.TextField(blank=True, help_text='Description of the purpose of the bill.'),
        ),
        migrations.AddField(
            model_name='billversion',
            name='lr_number',
            field=models.CharField(blank=True, help_text="Second part of Legislative Reference number (after '.').", max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time when the object was created.'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='extras',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Key-value store suitable for storing arbitrary information not covered elsewhere.'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='identifier',
            field=models.CharField(help_text="Identifier for the bill, as assigned by the Clerk's office (e.g., 'HB1', 'SB2').", max_length=100),
        ),
        migrations.AlterField(
            model_name='bill',
            name='lr_number',
            field=models.CharField(blank=True, help_text="First part of Legislative Reference number (before '.').", max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Date and time when the object was last updated.'),
        ),
        migrations.AlterField(
            model_name='billabstract',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time when the object was created.'),
        ),
        migrations.AlterField(
            model_name='billabstract',
            name='extras',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Key-value store suitable for storing arbitrary information not covered elsewhere.'),
        ),
        migrations.AlterField(
            model_name='billabstract',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Date and time when the object was last updated.'),
        ),
        migrations.AlterField(
            model_name='billaction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time when the object was created.'),
        ),
        migrations.AlterField(
            model_name='billaction',
            name='extras',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Key-value store suitable for storing arbitrary information not covered elsewhere.'),
        ),
        migrations.AlterField(
            model_name='billaction',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Date and time when the object was last updated.'),
        ),
        migrations.AlterField(
            model_name='billamendment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time when the object was created.'),
        ),
        migrations.AlterField(
            model_name='billamendment',
            name='extras',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Key-value store suitable for storing arbitrary information not covered elsewhere.'),
        ),
        migrations.AlterField(
            model_name='billamendment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Date and time when the object was last updated.'),
        ),
        migrations.AlterField(
            model_name='billsponsorship',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time when the object was created.'),
        ),
        migrations.AlterField(
            model_name='billsponsorship',
            name='extras',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Key-value store suitable for storing arbitrary information not covered elsewhere.'),
        ),
        migrations.AlterField(
            model_name='billsponsorship',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Date and time when the object was last updated.'),
        ),
        migrations.AlterField(
            model_name='billtitle',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time when the object was created.'),
        ),
        migrations.AlterField(
            model_name='billtitle',
            name='extras',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Key-value store suitable for storing arbitrary information not covered elsewhere.'),
        ),
        migrations.AlterField(
            model_name='billtitle',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Date and time when the object was last updated.'),
        ),
        migrations.AlterField(
            model_name='billversion',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time when the object was created.'),
        ),
        migrations.AlterField(
            model_name='billversion',
            name='extras',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Key-value store suitable for storing arbitrary information not covered elsewhere.'),
        ),
        migrations.AlterField(
            model_name='billversion',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Date and time when the object was last updated.'),
        ),
        migrations.AlterField(
            model_name='legislativesession',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time when the object was created.'),
        ),
        migrations.AlterField(
            model_name='legislativesession',
            name='extras',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text='Key-value store suitable for storing arbitrary information not covered elsewhere.'),
        ),
        migrations.AlterField(
            model_name='legislativesession',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Date and time when the object was last updated.'),
        ),
    ]
