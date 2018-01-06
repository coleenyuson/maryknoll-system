from __future__ import unicode_literals

from django.db import models

# Create your models here.
''' TAIL ENTITIES '''

#this might be temporary, will see for further changes
class Occupation(models.Model):
    occupation_name = models.CharField(max_length=200)

#this might be temporary, will see for further changes
class Schools(models.Model):
    school_name = models.CharField(max_length=200)

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
        

''' NON-TAIL ENTITIES '''

#this might be temporary, will see for further changes
class Parents(models.Model):
    p_lastnames = models.CharField(max_length=100)
    father_firstname = models.CharField(max_length=100)
    father_middlename = models.CharField(max_length=100)
    mother_firstname = models.CharField(max_length=100)
    mother_middlename = models.CharField(max_length=100)
    mother_occupation = models.ForeignKey(Occupation, on_delete = models.SET_NULL, null = True)
    father_occupation = models.ForeignKey(Occupation, on_delete = models.SET_NULL, null = True)



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
    #Foreign Keys
    parent_ID = models.ForeignKey(Parents, on_delete=models.SET_NULL, null=True)
    school_ID = models.ForeignKey(Schools, on_delete=models.CASCADE)
    class Meta:
        ordering = ["student_ID"]
        #allow only people with permissions
        #permissions = ((),)
        
    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s, %s - %s' % (self.student_ID, self.first_name, self.status)

class School_Year(models.Model):
	year_name = models.CharField(max_length=200)
	#status = models.CharField(max_length=50)
	date_start = models.DateField(auto_now = False)
	date_end = models.DateField(auto_now = False)

class Scholarship(models.Model):
	scholarship_name = models.CharField(max_length=200)
	amount = models.IntegerField()
	school_year = models.ForeignKey(School_Year, on_delete=models.CASCADE, default=0)
	validity =  models.IntegerField()
	status = models.CharField(max_length=50)
	scholar_type = models.IntegerField()
	
class SHS_Category(models.Model):
	category_name = models.CharField(max_length=200)
	type = models.IntegerField()
	status = models.CharField(max_length=50)
	
class Curriculum(models.Model):
    pass

class Subjects(models.Model):
	subject_ID = models.AutoField(primary_key=True)
	subject_name = models.CharField(max_length=200)
	status = models.CharField(max_length=50)
	curriculum = models.ForeignKey(Curriculum, on_delete = models.CASCADE)
	
class Prerequisites(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete = models.CASCADE)