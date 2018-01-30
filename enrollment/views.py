from django.shortcuts import render

# Create your views here.

def sectionList(request):
    
    return render(request,'enrollment/section-list.html')