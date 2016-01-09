# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_auto_20150809_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvgMarks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('overall', models.FloatField()),
                ('academics', models.FloatField()),
                ('sports', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='academics',
            name='average',
        ),
        migrations.RemoveField(
            model_name='sports',
            name='average',
        ),
        migrations.AlterField(
            model_name='college',
            name='datePublished',
            field=models.DateField(default=datetime.datetime(2015, 8, 9, 19, 35, 33, 428000, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='avgmarks',
            name='collegeId',
            field=models.ForeignKey(to='college.College'),
        ),
    ]
