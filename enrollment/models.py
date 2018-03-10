from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
import datetime
#import registration
#import administrative

# Create your models here.

ACTIVE = 'a'
ON_LEAVE = 'l'
INACTIVE = 'i'

ACADEMIC = 'c'
GOVT = 'g'
ATHLETIC = 'e'
OTHERS = 'o'

class TeacherDetails(models.Model):
    teacher_ID = models.AutoField(primary_key=True)
    employee_name = models.ForeignKey('administrative.Employee', on_delete= models.SET_NULL, null = True)
    units = models.IntegerField()
    class Meta:
        verbose_name = "Details of Teacher"
        
    def __str__(self):
        return str(self.employee_name)



class School_Year(models.Model):
	date_start = models.DateField(auto_now = True)
	
	class Meta:
	    verbose_name = "School Year"
	    
	def __str__(self):
	    return self.year_name

class YearLevel(models.Model):
    grade_level = models.CharField(max_length=200)
    
    def __str__(self):
        return self.grade_level

class Scholarship(models.Model):
	scholarship_name = models.CharField(max_length=200)
	school_year = models.ForeignKey(School_Year, on_delete=models.CASCADE, default=0)
	reductions = models.IntegerField()
	SCHOLARSHIP_CHOICES = (
        (ACADEMIC, 'Academic'),
        (GOVT, 'Government'),
        (ATHLETIC, 'Athletic'),
        (OTHERS, 'Others'),
    )
	scholarship_type = models.CharField(max_length=1,
        choices=SCHOLARSHIP_CHOICES,
        blank=False,
        default=OTHERS
        )
	
	class Meta:
	    verbose_name = "Scholarship"
	    
	def __str__(self):
	    return "%s for %s" % (self.scholarship_name, self.school_year)
#THIS ENTITY IS FOR MANY-TO-MANY 
class Scholarship_Registration(models.Model):
    student = models.ForeignKey('registration.Enrollment', on_delete = models.CASCADE)
    scholarship = models.ForeignKey(Scholarship, on_delete = models.CASCADE)
    
class Curriculum(models.Model):
    curriculum_ID = models.AutoField(primary_key=True)
    curriculum_year = models.DateField(default=datetime.date.today)
    STATUS_CHOICES=(
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    curriculum_status = models.CharField(max_length=1,
        choices=STATUS_CHOICES,
        blank=False,
        default=INACTIVE
        )
    class Meta:
        verbose_name = "Curriculum"
        
    def __str__(self):
        return "%s - %s" % (self.curriculum_year, self.curriculum_status)
        
    def get_abosulute_url(self):
	    return reverse('curriculum-list', kwargs={"id": self.id})

class Subjects(models.Model):
    subject_ID = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=200)
    units = models.IntegerField(null = True)
    curriculum = models.ForeignKey(Curriculum, on_delete = models.SET_NULL, null = True)
    year_level = models.ForeignKey(YearLevel, on_delete = models.CASCADE)
    class Meta:
        verbose_name = "Subject"
        
    def __str__(self):
        return self.subject_name
        
	
 
class Section(models.Model):
    section_ID = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=50)
    section_capacity = models.IntegerField()
    adviser = models.ForeignKey(TeacherDetails, on_delete = models.CASCADE)
    curriculum = models.ForeignKey(Curriculum, on_delete = models.SET_NULL, null = True)
    room = models.CharField(max_length=50)
    #Section status
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    section_status = models.CharField(max_length=1,
        choices=STATUS_CHOICES,
        blank=False,
        default=INACTIVE
        )
        
    class Meta:
        verbose_name = "Section"
    def __str__(self):
        return "%s - %s" % (self.curriculum,self.section_name)
    
    def get_abosulute_url(self):
	    return reverse('section-detail', kwargs={"id": self.id})
        
class Offering(models.Model):
	offering_ID = models.AutoField(primary_key=True)
	subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, default=0)
	teacher = models.ForeignKey(TeacherDetails, on_delete=models.CASCADE, default=0)
	school_year = models.ForeignKey(School_Year, on_delete=models.CASCADE, default=0)
	#Section bases on the year_level
	year_level = models.ForeignKey(YearLevel, on_delete=models.CASCADE, null = True)
	section = models.ForeignKey(Section, on_delete=models.CASCADE, null = True)
	
	class Meta:
	    verbose_name = "Offered Subject"
	def __str__(self):
	    return "%s - - - %s" % (self.subject, self.subject.subject_description)
	 
	def get_abosulute_url(self):
	    return reverse('subjectOffering-list', args=[str(self.offering_ID)])
	    
''' SCHEDULING WILL BE DEVELOPED IN A DIFFERENT APP '''

       
class Section_Enrollee(models.Model):
    enrollee = models.ForeignKey('registration.Enrollment', on_delete=models.CASCADE, default=0)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    student_status = models.CharField(max_length=1,
        choices=STATUS_CHOICES,
        blank=False,
        default=ACTIVE
        )
    class Meta:
	    verbose_name = "Enrollees in Sections"
    def __str__(self):
        return "%s enrolled in %s" % (self.enrollee, self.section)
    
class SHS_Subjects(models.Model):
    s_subjectName  = models.CharField(max_length=200)
    s_subjectDesc = models.CharField(max_length=200)
    s_desc = models.CharField(max_length=100)
    s_curriculum = models.ForeignKey(Curriculum, on_delete = models.CASCADE)
    #SHS track status
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    s_status = models.CharField(max_length=1,
        choices=STATUS_CHOICES,
        blank=False,
        default=INACTIVE
        )
        
    class Meta:
        verbose_name = "Senior High Subject"
        
    def __str__(self):
        return self.s_subjectName
        
        
class SHS_Offering(models.Model):
    offering_ID = models.AutoField(primary_key=True)
    subject = models.ForeignKey(SHS_Subjects, on_delete=models.CASCADE, default=0)
    teacher = models.ForeignKey(TeacherDetails, on_delete=models.CASCADE, default=0)
    school_year = models.ForeignKey(School_Year, on_delete=models.CASCADE, default=0)
	
    class Meta:
        verbose_name = "Offered Subjects for SHS"
    def __str__(self):
        return "%s - - - %s" % (self.subject, self.offering_ID)
