# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('average', models.FloatField()),
                ('courses', models.TextField()),
                ('avgFees', models.FloatField()),
                ('graduationRate', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datePublished', models.DateField(default=datetime.datetime(2015, 8, 9, 9, 54, 31, 508000, tzinfo=utc))),
                ('name', models.CharField(max_length=50)),
                ('university', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=50)),
                ('pin', models.BigIntegerField()),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=100)),
                ('coed', models.CharField(max_length=3)),
                ('seats', models.IntegerField()),
                ('acceptanceRate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('average', models.FloatField()),
                ('facilities', models.TextField()),
                ('popular', models.TextField()),
                ('collegeId', models.ForeignKey(to='college.College')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='academics',
            name='collegeId',
            field=models.ForeignKey(to='college.College'),
        ),
    ]
