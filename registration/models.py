from __future__ import unicode_literals

from django.db import models
from administrative.models import *
from enrollment.models import Curriculum, Offering, Scholarship

# Create your models here.
''' TAIL ENTITIES '''

class SHS_Subjects(models.Model):
    s_subjectName  = models.CharField(max_length=200)
    s_desc = models.CharField(max_length=100)
    #SHS track status
    STATUS_CHOICES = (
        ('a', 'Active'),
        ('n', 'Inactive'),
    )
    s_status = models.CharField(max_length=1,
        choices=STATUS_CHOICES,
        blank=False,
        default='n'
        )
        

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    #student status
    STATUS_CHOICES = (
        ('a', 'Active'),
        ('n', 'Inactive'),
    )
    status = models.CharField(max_length=1,
        choices=STATUS_CHOICES,
        blank=False,
        default='n'
        )
    #other attributes
    birthplace = models.CharField(max_length=200)
    birthdate = models.DateField(auto_now=False)
    home_addr = models.CharField(max_length=200)
    postal_addr = models.CharField(max_length=200)
    m_firstname = models.CharField(max_length=200)
    m_middlename = models.CharField(max_length=200)
    m_lastname = models.CharField(max_length=200)
    m_occcupation = models.CharField(max_length=200)
    f_firstname = models.CharField(max_length=200)
    f_middlename = models.CharField(max_length=200)
    f_lastname = models.CharField(max_length=200)
    f_occcupation = models.CharField(max_length=200)
    
    '''Model Configuration'''
    class Meta:
        ordering = ["student_ID"]
        #allow only people with permissions
        #permissions = ((),)
        
    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s, %s - %s' % (self.student_ID, self.first_name, self.status)

''' NON-TAIL ENTITIES '''

class Enrollment(models.Model):
	enrollment_ID = models.AutoField(primary_key=True)
	curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, default=0)
	student_ID = models.ForeignKey(Student, on_delete=models.CASCADE, default=0)
	scholarship_ID = models.ForeignKey(Scholarship, on_delete=models.CASCADE, default=0)
	student_type = models.IntegerField()
	
class Enrollment_Details(models.Model):
	enrollmentDetails_ID = models.AutoField(primary_key=True)
	enrollment_ID = models.ForeignKey(Enrollment, on_delete=models.CASCADE, default=0)
	offering_ID = models.ForeignKey(Offering, on_delete=models.CASCADE, default=0)

class Drop(models.Model):
	drop_ID = models.AutoField(primary_key=True)
	student_name = models.CharField(max_length=200)
	drop_date = models.DateTimeField(null=True, blank=True)
	curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, default=0)
	reason = models.CharField(max_length=500)
	status = models.CharField(max_length=2)
	approved_date = models.DateTimeField(null=True, blank=True)
	

	#HENLO BEBI
	#<3 
	#im double checkinggg
	#ping me lang if you're good :D
	#oki
	