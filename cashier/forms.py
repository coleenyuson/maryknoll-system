from django import forms
from .models import *
class EnrollmentBreakdownForm(forms.ModelForm):
    """Form definition for EnrollmentBreakdown."""

    class Meta:
        """Meta definition for EnrollmentBreakdownform."""
        model = EnrollmentBreakdown
        exclude = ()
