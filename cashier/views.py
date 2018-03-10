from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from registration.models import *
#FOR AJAX IMPORTS
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

# FEES AND ACCOUNTS || PARTICULARS # 
def openFeeAccount(request):
    return render(request, 'cashier/cashier-fees-and-accounts.html')
def tableFeeAccount(request):
    particulars_list = Particular.objects.all()
    #Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(particulars_list, 10)
    
    try:
        particulars = paginator.page(page)
    except PageNotAnInteger:
        particulars = paginator.page(1)
    except EmptyPage:
        particulars = paginator.page(paginator.num_pages)
        
    context = {'particulars': particulars}
    html_form = render_to_string('cashier/table-cashier-fees-and-accounts.html',
        context,
        request = request,
    )
    return JsonResponse({'html_form' : html_form})

def openFeeAccountAdd(request):
    return render(request, 'cashier/cashier-fees-and-accounts-add.html')
def formFeeAccountAdd(request):
    data = {'form_is_valid' : False }
    if request.method == 'POST':
        form = ParticularForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.particular_details = "Auto-generated"
            
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = ParticularForms()
    context = {'form': form}
    data['html_form'] = render_to_string('cashier/forms-cashier-fees-and-accounts-add.html',
        context,
        request=request,
    )
    return JsonResponse(data)
def openFeeAccountEdit(request,pk='pk'):
    particular = Particular.objects.get(particular_ID = pk)
    return render(request, 'cashier/cashier-fees-and-accounts-edit.html',{'particular':particular})

def formFeeAccountEdit(request,pk='pk'):
    particular = Particular.objects.get(particular_ID = pk)
    data = {'form_is_valid' : False }
    if request.method == 'POST':
        form = ParticularForms(request.POST,instance = particular)
        if form.is_valid():
            particular = form.save()
            particular.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = ParticularForms(instance = particular)
    context = {'form': form}
    data['html_form'] = render_to_string('cashier/forms-cashier-fees-and-accounts-add.html',
        context,
        request=request,
    )
    return JsonResponse(data)
    
# END PARTICULARS #
# ACCOUNTS #
def listAccounts(request):
    accounts = Account.objects.all()
    return render(request, 'accounts/accounts-list.html', {'accounts':accounts})


def addAccounts(request):
    if request.method == 'POST':
        form = AccountForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-accounts'))
    else:
        form = AccountForms()
    context = {'form': form}
    
    return render(request, 'accounts/add-accounts.html', context)

def listAccountParticulars(request):
    accounts = Account_Particular.objects.all()
    return render(request, 'accounts/accounts-particulars-list.html', {'accounts':accounts})

def addAccountParticulars(request):
    if request.method == 'POST':
        form = Account_ParticularForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-accounts'))
    else:
        form = Account_ParticularForms()
    context = {'form': form}
    
    return render(request, 'accounts/add-account-particulars.html', context)
# END ACCOUNTS #
# TRANSACTIONS #
from django.db.models import Sum

#Enrollment.objects.filter(section_name='St. Bernard').aggregate(Sum('enrolled'))

def listTransact(request):
    transacts = Transaction.objects.all()
    return render(request, 'transactions/transactions-list.html', {'transacts':transacts})


def addTransact(request):
    if request.method == 'POST':
        form = TransactionForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-transactions'))
    else:
        form = TransactionForms()
    context = {'form': form}
    
    return render(request, 'transactions/add-transactions.html', context)

def listTransactDetails(request):
    transacts = Transaction_Detail.objects.all()
    return render(request, 'transactions/transaction-details-list.html', {'transacts':transacts})

def addTransactDetails(request):
    curr_account = Account.objects.get(account_ID = 1)
    if request.method == 'POST':
        print request.POST['OR_num']
        form = Transaction_DetailForms(request.POST)
        if form.is_valid():
            #link this certain transaction detail to a transaction
            try:
                transact = Transaction.objects.get(OR_num=request.POST['OR_num']) 
            except Transaction.DoesNotExist:
                transact = Transaction(OR_num=request.POST['OR_num'], account_ID = curr_account)
                transact.save()
            post = form.save(commit=False)
            post.transact_ID = transact
            form.save()
            return HttpResponseRedirect(reverse('list-transactions'))
    else:
        form = Transaction_DetailForms()
        #Filters the foreign key fields
        form.fields["account_particular_ID"].queryset = Account_Particular.objects.filter(account_ID=curr_account)
    context = {'form': form}
    
    return render(request, 'transactions/add-transaction-details.html', context)
# END TRANSACTIONS #
# DAILY CASH #
def listDCash(request):
    pass

def addDCash(request):
    pass

def listDCashDetails(request):
    pass

def addDCashDetails(request):
    pass
# END DAILY CASH #
from django.db.models import Sum


def checkAccount(student):
    
    registration = Enrollment.objects.get(student_ID = student, SchoolYear = curr_school_year)
    
    if(registration):
        total_to_pay = 0.0
        total_paid = 0.0
        
        account = Account.objects.filter(enrollment_ID = registration)
        all_transactions = Transaction.objects.filter(account_ID = account)
        #Get all total payment made by student
        for transaction in all_transactions:
            payment = Transaction_Detail.objects.filter(transact_ID = transaction)
            total_paid += payment.amount_paid
        
        #Get all total payments needed by student
        total_to_pay = Account_Particular.objects.filter(year_level = registration.year_level).aggregate(Sum('to_pay'))
        
    else:
        pass
        #returns that a registration does not exist
        
    