from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Enrollment_Details)
admin.site.register(Drop)