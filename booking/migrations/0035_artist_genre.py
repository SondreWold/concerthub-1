# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0034_remove_artist_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.Genre'),
        ),
    ]
