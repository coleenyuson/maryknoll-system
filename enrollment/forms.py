from django import forms
from .models import *
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
    section_status= forms.CharField(widget=forms.RadioSelect(choices=STATUS_CHOICES))
    class Meta:
        model = Section
        exclude = ('section_ID',)