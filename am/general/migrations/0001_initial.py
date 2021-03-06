# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 03:44
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text=b'Date and time when the object was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text=b'Date and time when the object was last updated.')),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text=b'Key-value store suitable for storing arbitrary information not covered elsewhere.')),
                ('start_date', models.DateField(help_text="Date the Person's membership in the Organization starts.", max_length=10, null=True)),
                ('end_date', models.DateField(help_text="Date the Person's membership in the Organization ends.", max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text=b'Date and time when the object was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text=b'Date and time when the object was last updated.')),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text=b'Key-value store suitable for storing arbitrary information not covered elsewhere.')),
                ('name', models.CharField(help_text='Name of the Organization.', max_length=300)),
                ('classification', models.CharField(blank=True, choices=[('legislature', 'Legislature'), ('executive', 'Executive'), ('party', 'Party'), ('committee', 'Committee'), ('commission', 'Commission'), ('corporation', 'Corporation'), ('agency', 'Agency'), ('department', 'Department')], db_index=True, help_text='Categorizies the Organization', max_length=100)),
                ('parent', models.ForeignKey(help_text='Parent Organization of the Organization.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='general.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text=b'Date and time when the object was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text=b'Date and time when the object was last updated.')),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text=b'Key-value store suitable for storing arbitrary information not covered elsewhere.')),
                ('first_name', models.CharField(db_index=True, help_text='First name of the Person.', max_length=300)),
                ('middle_name', models.CharField(blank=True, db_index=True, help_text='Middle name (or initial) of the Person.', max_length=300)),
                ('last_name', models.CharField(db_index=True, help_text='Last name of the Person.', max_length=300)),
                ('suffix', models.CharField(blank=True, db_index=True, help_text="Name suffix (e.g., 'Jr.', 'Sr.', 'III') of the Person.", max_length=10)),
                ('nickname', models.CharField(blank=True, db_index=True, help_text='Last name of the Person.', max_length=300)),
                ('gender', models.CharField(blank=True, help_text='Gender of the Person, if known.', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'people',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text=b'Date and time when the object was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text=b'Date and time when the object was last updated.')),
                ('extras', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, help_text=b'Key-value store suitable for storing arbitrary information not covered elsewhere.')),
                ('label', models.CharField(help_text='A label describing the Post (e.g., State Senate 10).', max_length=300)),
                ('role', models.CharField(blank=True, help_text='The function the holder of the Post fulfills (e.g., Senator).', max_length=300)),
                ('district_number', models.IntegerField(help_text='Number identifying the political district represented by the Post.', null=True)),
                ('organization', models.ForeignKey(help_text='References the Organization in which the Post exists.', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='general.Organization')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='organization',
            field=models.ForeignKey(help_text='References the Organization in which the Person is a member.', on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='general.Organization'),
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(help_text='References the Person who is a member in the Organization.', on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='general.Person'),
        ),
        migrations.AddField(
            model_name='membership',
            name='post',
            field=models.ForeignKey(help_text='References to the Post held by the member, if applicable.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='general.Post'),
        ),
        migrations.AlterIndexTogether(
            name='post',
            index_together=set([('organization', 'label')]),
        ),
        migrations.AlterIndexTogether(
            name='membership',
            index_together=set([('organization', 'person', 'post')]),
        ),
    ]
