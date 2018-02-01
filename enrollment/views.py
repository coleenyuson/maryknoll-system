from django.shortcuts import render
from .models import *

# Create your views here.

def sectionList(request):
    section_list = Section.objects.all()
    context = {
        'section_list' : section_list
    }
    return render(request,'enrollment/section-list.html', context)