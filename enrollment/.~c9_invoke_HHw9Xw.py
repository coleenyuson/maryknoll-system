from django import forms
from .models import *
from enrollment.models import *

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

ACTIVE = 'a'
ON_LEAVE = 'o'
INACTIVE = 'i'
STATUS_CHOICES = (
    (ACTIVE, 'Active'),
    (INACTIVE, 'Inactive'),
)
class SectionForms(forms.ModelForm):
    class Meta:
        model = Section
        exclude = ('section_ID', 'section_status',)
        
class SubjectForm(forms.ModelForm):
    """Curriculum-details-create."""

    class Meta:
        """Meta definition for Subjectform."""

        model = Subjects
        exclude = ('curriculum',)

        
class ScholarshipForms(forms.ModelForm):
    class Meta:
        model = Scholarship
        exclude = ('pk',)
        
class SubjectOfferingForms(forms.ModelForm):
    class Meta:
        model = Offering
        exclude = ('pk','school_year')

class School_YearForm(forms.ModelForm):
    """Form definition for School_Year."""

    class Meta:
        """Meta definition for School_Yearform."""

        model = School_Year
        exclude = ('date_start',)

class StudentSectionForm(forms.ModelForm):
    student_ID = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        widget=autocomplete.ModelSelect2(url='country-autocomplete')
    )
    class Meta:
        model = Student
        fields = ('student_ID')