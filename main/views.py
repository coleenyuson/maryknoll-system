from django.shortcuts import render
from django.views import generic
from enrollment.models import School_Year
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@login_required
def index(request):
    return render(request,'admin-dashboard.html',)
    
@login_required
def settings(request):
    try:
        latest_sy = School_Year.objects.latest('date_start')
    except:
        latest_sy = None
    return render(request,'admin-settings.html', context={'school_year':latest_sy})