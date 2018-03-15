# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-15 06:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='scholarship',
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enrollment.Section'),
        ),
    ]
