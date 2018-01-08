# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-07 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_ID', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('emp_type', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Promissory',
            fields=[
                ('promissory_ID', models.AutoField(primary_key=True, serialize=False)),
                ('promisorry_name', models.CharField(max_length=200)),
                ('reason', models.CharField(max_length=500)),
                ('date_filed', models.DateTimeField(blank=True, null=True)),
                ('date_approved', models.DateTimeField(blank=True, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]