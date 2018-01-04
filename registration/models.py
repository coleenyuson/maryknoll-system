from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    student_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
    STATUS_CHOICES = (
        ('a', 'Active'),
        ('n', 'Inactive'),
    )
    status = models.CharField(max_length=1,
        choices=STATUS_CHOICES,
        blank=False,
        default='n'
        )
        
    class Meta:
        ordering = ["student_ID"]
        #allow only people with permissions
        #permissions = ((),)
        
    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s, %s - %s' % (self.student_ID, self.first_name, self.status)
