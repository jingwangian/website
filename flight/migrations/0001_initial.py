# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-14 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlightPriceQueryTask',
            fields=[
                ('flight_id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('execute_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'flight_price_query_task',
            },
        ),
        migrations.CreateModel(
            name='FlightTaskStatus',
            fields=[
                ('total_tasks', models.IntegerField(blank=True, null=True)),
                ('success_tasks', models.IntegerField(blank=True, null=True)),
                ('total_records', models.IntegerField(blank=True, null=True)),
                ('workers', models.IntegerField(blank=True, null=True)),
                ('task_start_time', models.DateTimeField(blank=True, null=True)),
                ('task_finished_time', models.DateTimeField(blank=True, null=True)),
                ('execute_date', models.DateField(primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'flight_task_status',
            },
        ),
    ]
