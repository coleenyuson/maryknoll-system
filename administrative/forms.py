from django import forms
from .models import *
from enrollment.models import *
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

class EmployeeForms(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ('employee_ID',)