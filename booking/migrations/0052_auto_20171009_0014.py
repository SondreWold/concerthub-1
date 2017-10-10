# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0051_auto_20171008_2346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookingoffer',
            options={'ordering': ('offering_date', 'offering_stage')},
        ),
        migrations.AlterModelOptions(
            name='timeslot',
            options={'ordering': ('start_date',)},
        ),
        migrations.AlterField(
            model_name='concert',
            name='sold_tickets',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
