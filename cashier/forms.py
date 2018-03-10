from django import forms
from .models import *

class ParticularForms(forms.ModelForm):
    class Meta:
        model = Particular
        exclude = ('particular_ID','particular_details',)
''' ACCOUNTS FORMS '''

class AccountForms(forms.ModelForm):
    class Meta:
        model = Account
        exclude = ('account_ID',)

class Account_ParticularForms(forms.ModelForm):
    class Meta:
        model = Account_Particular
        exclude = ('account_particular_ID',)
        
''' TRANSACTION FORMS '''

class TransactionForms(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ('date_time_created',)

class Transaction_DetailForms(forms.ModelForm):
    class Meta:
        model = Transaction_Detail
        exclude = ('transaction_detail_ID','transact_ID',)
        
class Daily_CashForms(forms.ModelForm):
    class Meta:
        model = Daily_Cash
        exclude = ('daily_cash_ID',)