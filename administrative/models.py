from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employee(models.Model):
	employee_ID = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	emp_type = models.IntegerField()
	status = models.CharField(max_length=50)