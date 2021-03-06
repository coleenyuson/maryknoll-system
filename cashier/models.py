from __future__ import unicode_literals

from django.db import models

#SIGNALS = TRIGGERS
from django.db.models.signals import post_save
# Create your models here.


''' PARTICULARS '''

class Particular(models.Model):
    particular_ID = models.AutoField(primary_key=True)
    particular_name = models.CharField(max_length=100)
    particular_details = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.particular_name


''' STUDENT ACCOUNTS: 
    Why is it modeled this way?
        A STUDENT DOESNT HOLD ANY ACCOUNT, BUT HIS CURRENT REGISTRATION DOES.
        So this means, after this school year, a new account will be made again for a certain registration
        This supports archived view of a student's previous account
        
    Explanations for each entity:
    - Account:
        This holds the student details, and account_ID of a certain student registration.
    - Account_Particular:
        So, EVERY student has a DIFFERENT AMOUNT TO BE PAID FOR EVERY PARTICULAR. 
        It is designed this way so that we can explicitly show what are the things that a student must/ is able to pay.
        account_particular_ID = primary key of this table
        account_ID = what account is this certain particular assigned to?
        to_pay = how much does the user has to pay for this certain particular. This is a USER INPUT.
        particular_ID = What certain particular is this requirement?
'''

class Account(models.Model): #should only be created through triggers
    account_ID = models.AutoField(primary_key=True)
    enrollment_ID = models.CharField(max_length=200) #Foreign key to a certain enrollee
    def __str__(self):
        return "%s's Account" %(self.enrollment_ID)

class Account_Particular(models.Model): #we can consider this as the REQUIREMENTS table
    account_particular_ID = models.AutoField(primary_key=True)
    account_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
    to_pay = models.FloatField()
    particular_ID = models.ForeignKey(Particular, on_delete=models.CASCADE)
    def __str__(self):
        return "%s of %s" %(self.particular_ID,self.account_ID)

''' TRANSACTIONS:
    Why is it modeled this way?
        This is modeled in a way it adapts to daily, dynamic, and adjustable payment process.
    
    Explanation to every entity:
    - Transaction:
        -- A transaction entity is the receipt itself,
        DATE-TIME = date and time the transaction was made
        account_ID = A transaction must be linked to a student-Account, so the payment could be recorded.
        OR_NUM = the cashier inputs this number
        
    - Transaction_Detail:
        -- A single transaction records the amount the customer pays, but we MUST record to WHAT IS HE PAYING TO?
        transact_ID = Record this particular AMOUNT of PAYMENT FOR a CERTAIN PARTICULAR AND PLACE IT ON A CERTAIN TRANSACTION PAPER (RECEIPT)
        amount_paid = Amount the customer PAID FOR A CERTAIN PARTICULAR
        account_particular_ID = this means that THE USER CAN ONLY PAY FOR PARTICULARS THAT IS IN HIS ACCOUNTS
'''

class Transaction(models.Model):
    transact_ID = models.AutoField(primary_key=True)
    date_time_created = models.DateTimeField(auto_now=True)
    account_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
    OR_num = models.BigIntegerField()
    def __str__(self):
        return str(self.account_ID)
    
class Transaction_Detail(models.Model):
    transaction_detail_ID = models.AutoField(primary_key=True)
    transact_ID = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    amount_paid = models.FloatField()
    account_particular_ID = models.ForeignKey(Particular, on_delete=models.CASCADE)
    def __str__(self):
        return "%s's purchase of %s" % (self.transact_ID, self.account_particular_ID)

''' CASH LOGS and REPORTS:
    Why is it modelled this way?
        This is for recording purposes, THIS SHOULD NEVER BE INPUTTED BY THE CASHIER, therefore must be AUTO-GENERATED by the system using functions or whatnot
    Explanations for every entity:
    -Daily_Cash:
        This holds the GENERAL INFORMATION for every single daily_cash_details like DATE(auto-date) and DCR no.(which is inputted)
        DATE = This is auto-generated. The user only needs to input the DCR No.
        DCR_no = The user inputs DCR_no here
    - Daily_Cash_Detail:
        This is EVERY, SINGLE, ROW, IN, THE, DAILY, CASH, FLOW, REPORT. The total of these all is going to be SUMMED up at the end.
        transact_ID = what certain transaction did this money came from?
        cash = AUTO-GENERATED. ALWAYS UPDATED.
'''

class Daily_Cash(models.Model):
    daily_cash_ID = models.AutoField(primary_key=True)
    date_today = models.DateField(auto_now=True)
    DCR_num = models.CharField(max_length=255, default=None,null=True)
    
class Daily_Cash_Detail(models.Model):
    daily_cash_ID = models.ForeignKey(Daily_Cash, on_delete=models.CASCADE)
    transact_ID = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    cash = models.FloatField()
    


'''SIGNALS'''