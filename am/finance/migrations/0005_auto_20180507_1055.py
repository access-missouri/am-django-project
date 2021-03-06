# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 15:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_tag'),
        ('finance', '0004_auto_20180424_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financeentity',
            old_name='linked_person',
            new_name='canonical_person',
        ),
        migrations.AddField(
            model_name='financeentity',
            name='canonical_organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='finance_entities', to='general.Organization'),
        ),
        migrations.AddField(
            model_name='financeentity',
            name='related_people',
            field=models.ManyToManyField(blank=True, related_name='finance_entities_all', to='general.Person'),
        ),
    ]
