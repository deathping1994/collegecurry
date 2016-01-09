# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='datePublished',
            field=models.DateField(default=datetime.datetime(2015, 8, 9, 10, 23, 48, 54000, tzinfo=utc)),
        ),
    ]
