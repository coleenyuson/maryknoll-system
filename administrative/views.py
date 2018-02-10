from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmployeeForms

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import *

@login_required
def index(request):
    pass

@login_required
def userList(request):
    return render(request, 'administrative/admin-employee-list.html')

def addEmployeeProfile(request):
    return render(request, 'administrative/admin-employee-list-add.html')
    
#AJAX VIEWS --------------------------------------------------------------------
from django.template.loader import render_to_string
from django.http import JsonResponse

def tableEmployeeList(request):
    employee_list = Employee.objects.all()
    #Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(employee_list, 10)
    
    try:
        employee = paginator.page(page)
    except PageNotAnInteger:
        employee = paginator.page(1)
    except EmptyPage:
        employee = paginator.page(paginator.num_pages)
        
    context = {'employee_list': employee}
    html_form = render_to_string('administrative/table-employee-list.html',
        context,
        request = request,
    )
    return JsonResponse({'html_form' : html_form})

def createEmployeeProfile(request):
    data = {'form_is_valid' : False }
    try:
        last_employee = Employee.objects.latest('student_ID')
    except:
        last_employee = None
    if request.method == 'POST':
        form = EmployeeForms(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = EmployeeForms()
    context = {'form': form, 'employee':last_employee}
    data['html_form'] = render_to_string('administrative/forms-employee-create.html',
        context,
        request=request,
    )
    return JsonResponse(data)