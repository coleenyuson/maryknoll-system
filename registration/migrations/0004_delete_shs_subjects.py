# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-07 16:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20180107_1558'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SHS_Subjects',
        ),
    ]