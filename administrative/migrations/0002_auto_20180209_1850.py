# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-10 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enrollment', '0001_initial'),
        ('administrative', '0001_initial'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promissory',
            name='schoolYr_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='enrollment.School_Year'),
        ),
        migrations.AddField(
            model_name='promissory',
            name='student_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='registration.Student'),
        ),
    ]
