# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-07 15:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drop',
            options={'verbose_name': 'Drop'},
        ),
        migrations.AlterModelOptions(
            name='enrollment',
            options={'verbose_name': 'Enrollment'},
        ),
        migrations.AlterModelOptions(
            name='enrollment_details',
            options={'verbose_name': 'Enrollment_Details'},
        ),
        migrations.AlterModelOptions(
            name='shs_subjects',
            options={'verbose_name': 'Subjects for SHS'},
        ),
    ]