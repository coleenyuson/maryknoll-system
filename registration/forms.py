from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class StudentForms(forms.ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), 
                                 input_formats=('%d/%m/%Y',))
    class Meta:
        model = Student
        fields = ('first_name', 'last_name','gender',
        'birthplace','birthdate','home_addr','postal_addr','m_firstname',
        'm_middlename','m_lastname','m_occcupation','f_firstname','f_middlename',
        'f_lastname','f_occupation','guardian','guardian_addr','last_school')
        
class RegistrationForms(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ('section', 'student','scholarship','student_type',)