# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-20 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_tag'),
        ('legislative', '0018_auto_20180420_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='tags',
            field=models.ManyToManyField(blank=True, to='general.Tag'),
        ),
    ]