from __future__ import unicode_literals

from django.db import models
#import registration

# Create your models here.
'''TAIL ENTITIES'''
class FeesAccounts(models.Model):
    fa_ID = models.AutoField(primary_key = True)
    fa_name = models.CharField(max_length = 200)
    amount = models.FloatField()
    
    class Meta:
        verbose_name = "List of Fees and Account"
        
    def __str__(self):
        return self.fa_name
    
'''NON-TAIL ENTITIES'''

CASH = 'c'
CHECK = 'q'
OTHERS = 'o'

class Payments(models.Model):
    payment_ID = models.AutoField(primary_key=True)
    enrollment_ID = models.ForeignKey('registration.Enrollment', on_delete = models.SET_NULL, null = True)
    payment_date = models.DateField()
    total_amount = models.FloatField()
    TYPE_CHOICES = (
        (CASH, 'Cash'),
        (CHECK, 'Check'),
        (OTHERS, 'Others'),
        )
    
    payment_type = models.CharField(max_length=1,choices=TYPE_CHOICES,blank=False,default=CASH)
    payment_note = models.CharField(max_length=200)
    OR_number = models.IntegerField()
    
    class Meta:
        verbose_name = "Payment Log"
        
    def __str__(self):
        return "%s as of %s" % (self.enrollment_ID, str(self.payment_date))
    
class PaymentDetails(models.Model):
    pdetails_ID = models.AutoField(primary_key=True)
    payment_ID = models.ForeignKey(Payments, on_delete = models.SET_NULL, null = True)
    fa_ID = models.ForeignKey(FeesAccounts, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = "Paid fees and account"
        
    def __str__(self):
        return "%s - %s Date: %s" % (self.payment_ID, self.fa_ID, self.payment_ID.payment_date)