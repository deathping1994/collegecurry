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
            name='Reviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateAdded', models.DateField(default=datetime.datetime(2015, 8, 9, 10, 23, 48, 60000, tzinfo=utc))),
                ('authorName', models.CharField(max_length=25)),
                ('authorEmail', models.EmailField(max_length=100)),
                ('authorYear', models.IntegerField()),
                ('authorCourse', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=20, choices=[(b'Academics', b'Academics'), (b'Sports', b'Sports')])),
                ('marks', models.FloatField(default=b'1.00')),
                ('review', models.TextField()),
                ('collegeId', models.ForeignKey(to='college.College')),
            ],
        ),
    ]
