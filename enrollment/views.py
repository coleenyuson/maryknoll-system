from django.shortcuts import render
from .models import *

# Create your views here.

def sectionList(request):
    section_list = Section.objects.all()
    context = {
        'section_list' : section_list
    }
    return render(request,'enrollment/section-list.html', context)
    
def addSection(request):
    return render(request, 'enrollment/section-details-add.html')
    
def sectionDetails(request, pk='pk'):
    student = get_object_or_404(Student, pk=pk)
    
    return render(request, 'enrollment/student-details.html', {'student': student, 'record':last_record})