# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-08 02:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enrollment', '0006_auto_20180107_1635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacherdetails',
            old_name='employee_name',
            new_name='employee_ID',
        ),
    ]