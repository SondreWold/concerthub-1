# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0059_auto_20171009_1329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='concert',
            options={'ordering': ('time_slot__start_date', 'time_slot__stage', 'artist')},
        ),
    ]
