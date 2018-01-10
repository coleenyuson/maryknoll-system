from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
#import registration
#import administrative

# Create your models here.

class School_Year(models.Model):
	year_name = models.CharField(max_length=200)
	#status = models.CharField(max_length=50)
	date_start = models.DateField(auto_now = True)
	date_end = models.DateField(null=True, blank=True)
	
	class Meta:
	    verbose_name = "School Year"
	    
	def __str__(self):
	    return self.year_name

class Scholarship(models.Model):
	scholarship_name = models.CharField(max_length=200)
	amount = models.IntegerField()
	school_year = models.ForeignKey(School_Year, on_delete=models.CASCADE, default=0)
	validity =  models.BooleanField(default = False)
	scholar_type = models.IntegerField()
	
	class Meta:
	    verbose_name = "Scholarship"
	    
	def __str__(self):
	    return self.scholarship_name
	
	'''Scholar Type(INT?) and Scholar Name? What's the difference '''
	
class SHS_Category(models.Model):
	category_name = models.CharField(max_length=200)
	type = models.IntegerField()
	status = models.CharField(max_length=50)
	
	class Meta:
	    verbose_name = "Senior High Category"
	
class Curriculum(models.Model):
    curriculum_ID = models.AutoField(primary_key=True)
    curriculum_year = models.IntegerField()
    school_year = models.ForeignKey(School_Year, on_delete=models.CASCADE, default=0)
    
    class Meta:
        verbose_name = "Curriculum"
        
    def __str__(self):
        return str(self.school_year)
    '''Fix this:
        suggestions - Add Curriculum name, change curriculum year to DateField.'''

class Subjects(models.Model):
	subject_ID = models.AutoField(primary_key=True)
	subject_name = models.CharField(max_length=200)
	status = models.CharField(max_length=50)
	curriculum = models.ForeignKey(Curriculum, on_delete = models.CASCADE)
	
	class Meta:
	    verbose_name = "Subject"
	    
	def __str__(self):
	    return self.subject_name
	    
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
        
    class Meta:
        verbose_name = "Section"
    def __str__(self):
        return self.section_name
    
    def get_absolute_url(self):
		return reverse("section-edit", kwargs={"id": self.id})
    '''Add section 'capacity' and 'grade level'... Choose Grade Level -> Choose name -> Choose Status -> Add capacity'''
    

class TeacherDetails(models.Model):
    teacher_ID = models.AutoField(primary_key=True)
    employee_name = models.ForeignKey('administrative.Employee')
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
        
    advised_section = models.ForeignKey(Sections, on_delete = models.SET_NULL, null = True)
        
    class Meta:
        verbose_name = "Details of Teacher"
        
    def __str__(self):
        return str(self.employee_name)

class Offering(models.Model):
	offering_ID = models.AutoField(primary_key=True)
	subject_ID = models.ForeignKey(Subjects, on_delete=models.CASCADE, default=0)
	teacher = models.ForeignKey(TeacherDetails, on_delete=models.CASCADE, default=0)
	schoolYr_ID = models.ForeignKey(School_Year, on_delete=models.CASCADE, default=0)
	
	class Meta:
	    verbose_name = "Offered Subject"
	def __str__(self):
	    return "%s - - - %s" % (self.subject_ID, self.offering_ID)
	    
''' Add Scheduling, Time Period attributes, SCHEDULING MODULE IMPLEMENTATION'''
	
class Prerequisites(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete = models.CASCADE)
    
    class Meta:
        verbose_name = "Prerequisite"
    
  
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
        
    class Meta:
        verbose_name = "Senior High Subject"
        
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.s_subjectName
    
    def get_absolute_url(self):
		return reverse("shsSubj-edit", kwargs={"id": self.id})
        