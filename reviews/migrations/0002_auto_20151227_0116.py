# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 19:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='dateAdded',
            field=models.DateField(default=datetime.datetime(2015, 12, 26, 19, 46, 31, 771108, tzinfo=utc)),
        ),
    ]
