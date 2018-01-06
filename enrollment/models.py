from __future__ import unicode_literals

from django.db import models
from registration.models import Student
from administrative.models import Employee

# Create your models here.

class School_Year(models.Model):
	year_name = models.CharField(max_length=200)
	#status = models.CharField(max_length=50)
	date_start = models.DateField(auto_now = False)
	date_end = models.DateField(auto_now = False)

class Scholarship(models.Model):
	scholarship_name = models.CharField(max_length=200)
	amount = models.IntegerField()
	school_year = models.ForeignKey(School_Year, on_delete=models.CASCADE, default=0)
	validity =  models.BooleanField(default = False)
	scholar_type = models.IntegerField()
	
class SHS_Category(models.Model):
	category_name = models.CharField(max_length=200)
	type = models.IntegerField()
	status = models.CharField(max_length=50)
	
class Curriculum(models.Model):
    curriculum_ID = models.AutoField(primary_key=True)
    curriculum_year = models.IntegerField()
    school_year = models.ForeignKey(School_Year, on_delete=models.CASCADE, default=0)

class Subjects(models.Model):
	subject_ID = models.AutoField(primary_key=True)
	subject_name = models.CharField(max_length=200)
	status = models.CharField(max_length=50)
	curriculum = models.ForeignKey(Curriculum, on_delete = models.CASCADE)

class Offering(models.Model):
	offering_ID = models.AutoField(primary_key=True)
	subject_ID = models.ForeignKey(Subjects, on_delete=models.CASCADE, default=0)
	teacher = models.ForeignKey(Employee, on_delete=models.CASCADE, default=0)
	schoolYr_ID = models.ForeignKey(School_Year, on_delete=models.CASCADE, default=0)
	
class Prerequisites(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete = models.CASCADE)
    
class Sections(models.Model):
    section_ID = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=50)
    #Section status
    STATUS_CHOICES = (
        ('a', 'Active'),
        ('n', 'Inactive'),
    )
    section_status = models.CharField(max_length=1,
        choices=STATUS_CHOICES,
        blank=False,
        default='n'
        )
        
class TeacherDetails(models.Model):
    teacher_ID = models.AutoField(primary_key=True)
    employee_ID = models.ForeignKey(Employee, on_delete = models.CASCADE)
    units = models.IntegerField()
    #teacher status
    STATUS_CHOICES = (
        ('a', 'Active'),
        ('n', 'Inactive'),
    )
    section_status = models.CharField(max_length=1,
        choices=STATUS_CHOICES,
        blank=False,
        default='n'
        )
        
    advised_section = models.ForeignKey(Sections, on_delete = models.SET_NULL)
        
