from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Particular)
class ParticularAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Particular._meta.get_fields()]