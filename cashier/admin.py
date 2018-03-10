from django.contrib import admin

# Register your models here.
from cashier.models import * 

@admin.register(Particular)
class ParticularAdmin(admin.ModelAdmin):
    list_display = ['particular_ID','particular_name','particular_details',]
    
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['account_ID','enrollment_ID','date_time_created',]
    
@admin.register(Account_Particular)
class AccPartAdmin(admin.ModelAdmin):
    list_display = ['account_particular_ID','year_level','to_pay','particular_ID',]