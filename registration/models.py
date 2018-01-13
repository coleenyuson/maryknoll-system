from __future__ import unicode_literals

from django.db import models
from datetime import datetime
#from administrative.models import *
#from enrollment.models import Curriculum, Offering, Scholarship

# Create your models here.
''' TAIL ENTITIES '''

class Student(models.Model):
    student_ID = models.AutoField(primary_key=True)
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
    guardian = models.CharField(max_length=200)
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

PAID = 'PAID'
INCOMPLETE = 'INCOMPLETE'
NO_PAY = 'NOT PAID'

class Enrollment(models.Model):
    enrollment_ID = models.AutoField(primary_key=True)
    section = models.ForeignKey('enrollment.Section', on_delete=models.CASCADE, default=0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=0)
    scholarship = models.ForeignKey('enrollment.Scholarship', on_delete=models.CASCADE, default=0)
    '''Type enum '''
    TYPE_CHOICES = (
        (PAID,'Paid'),
        (INCOMPLETE,'Incomplete'),
        (NO_PAY,'No Payment Yet'),)
    
    student_type = models.CharField(max_length=1,choices=TYPE_CHOICES,blank=False,default='n')
    
    
    class Meta:
        verbose_name = "Enrollment"
        
    def __str__(self):
        return "%s enrolled under %s" % (self.student_ID, self.curriculum)


class Drop(models.Model):
	drop_ID = models.AutoField(primary_key=True)
	student_name = models.CharField(max_length=200)
	drop_date = models.DateField(auto_now=True)
	curriculum = models.ForeignKey('enrollment.Curriculum', on_delete=models.CASCADE, default=0)
	reason = models.CharField(max_length=500)
	status = models.CharField(max_length=2)
	approved_date = models.DateTimeField(null=True, blank=True)
	
	class Meta:
	    verbose_name = "Drop"
	