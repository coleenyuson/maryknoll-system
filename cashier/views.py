from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

# FOR AJAX IMPORTS
from django.template.loader import render_to_string
from django.http import JsonResponse

# Global Functions


def paginateThis(request, obj_list, num):
    # Pagination. Send request, the list you want to paginate, and number of items per page.
    # This returns a limited list with pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(obj_list, num)
    try:
        lists = paginator.page(page)
    except PageNotAnInteger:
        lists = paginator.page(1)
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)
    return lists


def ajaxTable(request, template, context, data=None):
    # For templates that needs ajax
    html_form = render_to_string(template,
                                 context,
                                 request=request,
                                 )
    if data:
        data['html_form'] = html_form
    else:
        data = {'html_form': html_form}
    return JsonResponse(data)


def getLatest(model, attribute):
    # Get latest record of a model, basing on a certain attribute
    # Returns an instance
    try:
        latest = model.objects.latest(attribute)
    except:
        latest = None
    return latest


def updateInstance(request, modelForm, instance):
    if request.method == 'POST':
        form = modelForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()
            instance.save()
    else:
        form = modelForm(instance=instance)
    return form


# Views
def index(request):
    return render(request, 'index.html')

# FEES AND ACCOUNTS || PARTICULARS #


def openFeeAccount(request, template='cashier/fees-and-accounts/cashier-fees-and-accounts.html'):
    return render(request, template)


def tableFeeAccount(request, template='cashier/fees-and-accounts/table-cashier-fees-and-accounts.html'):
    particulars_list = EnrollmentBreakdown.objects.all()
    # Pagination
    page = request.GET.get('page', 1)
    particulars = paginateThis(request, particulars_list, 10)
    context = {'particulars': particulars}

    return ajaxTable(request, template, context)


def openFeeAccountAdd(request, template='cashier/fees-and-accounts/cashier-fees-and-accounts-add.html'):
    return render(request, template)


def formFeeAccountAdd(request, template='cashier/fees-and-accounts/forms-cashier-fees-and-accounts-add.html'):
    data = {'form_is_valid': False}
    if request.method == 'POST':
        form = EnrollmentBreakdownForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.particular_details = "Auto-generated"

            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = EnrollmentBreakdownForm()
    context = {'form': form}
    return ajaxTable(request, template, context, data)


def openFeeAccountEdit(request, pk='pk', template='cashier/fees-and-accounts/cashier-fees-and-accounts-edit.html'):
    particular = EnrollmentBreakdown.objects.get(pk=pk)
    context = {'particular': particular}
    return render(request, template, context)


def formFeeAccountEdit(request, pk='pk', template='cashier/fees-and-accounts/forms-cashier-fees-and-accounts-edit.html'):
    particular = EnrollmentBreakdown.objects.get(pk=pk)
    data = {'form_is_valid': False}
    if request.method == 'POST':
        form = EnrollmentBreakdownForm(request.POST, instance=particular)
        if form.is_valid():
            particular = form.save()
            particular.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = EnrollmentBreakdownForm(instance=particular)
    context = {'form': form, 'particular': particular}
    return ajaxTable(request, template, context, data)

# END PARTICULARS #
# ACCOUNTS #


# END ACCOUNTS #
# TRANSACTIONS #
from django.db.models import Sum
def transactionView(request,pk='pk',template='cashier/transactions/payment-transaction.html'):
    context = {}
    return render(request,template,context)

def summaryView(request, template="cashier/transactions/"):

    return ajaxTable(request,template,context)
#Enrollment.objects.filter(section_name='St. Bernard').aggregate(Sum('enrolled'))

# END DAILY CASH #
