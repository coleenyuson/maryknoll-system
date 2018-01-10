from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
#from registration.models import Student
#from enrollment.models import School_Year

# Create your models here.

class Employee(models.Model):
	employee_ID = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	emp_type = models.IntegerField()
	status = models.CharField(max_length=50)
	
	class Meta:
		verbose_name = "Employee"
		
	def __str__(self):
		return self.first_name
		
	def get_absolute_url(self):
		return reverse("emp-edit", kwargs={"id": self.employee_ID})
        
'''Add choices to Employee_Type(NOT INT): Cashier, Admin, etc. also, add departments'''
	
class Promissory(models.Model):
	promissory_ID = models.AutoField(primary_key=True)
	promisorry_name = models.CharField(max_length=200)
	reason = models.CharField(max_length=500)
	date_filed =models.DateTimeField(null=True, blank=True)
	date_approved = models.DateTimeField(null=True, blank=True)
	deadline = models.DateTimeField(null=True, blank=True)
	student_ID = models.ForeignKey('registration.Student', on_delete=models.CASCADE, default=0)
	schoolYr_ID = models.ForeignKey('enrollment.School_Year', on_delete=models.CASCADE, default=0)
	status = models.CharField(max_length=50)
	
	class Meta:
		verbose_name = "Promissory Note"