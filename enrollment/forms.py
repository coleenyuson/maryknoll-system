from django import forms
from .models import *
from enrollment.models import *
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

class CurriculumForms(forms.ModelForm):
    class Meta:
        model = Curriculum
        exclude = ('curriculum_ID',)