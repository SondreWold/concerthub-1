# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0064_auto_20171010_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='artist_rev',
            field=models.TextField(blank=True),
        ),
    ]