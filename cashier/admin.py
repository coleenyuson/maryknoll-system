from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(FeesAccounts)
admin.site.register(Payments)
admin.site.register(PaymentDetails)