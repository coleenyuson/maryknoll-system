from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(School_Year)
admin.site.register(Scholarship)
admin.site.register(SHS_Category)
admin.site.register(Curriculum)
admin.site.register(Subjects)
admin.site.register(Offering)
admin.site.register(Sections)
admin.site.register(TeacherDetails)
admin.site.register(SHS_Subjects)