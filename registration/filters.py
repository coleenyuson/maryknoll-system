from .models import *
import django_filters

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['student_ID', 'first_name', 'last_name','middle_name','student_level','status' ]