from django.shortcuts import render
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@login_required
def index(request):
    return render(request,'index.html',)
    
@login_required
def settings(request):
    return render(request,'admin-settings.html',)