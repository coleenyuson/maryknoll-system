from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from .models import *
from .forms import StudentForms, RegistrationForms


@login_required
def index(request):
    pass
    #return render(request,'/registration/index.html',)
@login_required
def registrationList(request):
    form = StudentForms(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit = False)
        post.status = 'Inactive'
        form.save()

    # notice this comes after saving the form to pick up new objects
    student_list = Student.objects.all()
    #Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(student_list, 10)
    
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    
    return render(request, 'registrar/student-registration-list.html', {'student_list': students, 'form': form})
@login_required
def studentDetails(request, pk='pk'):
    student = get_object_or_404(Student, pk=pk)
    form = RegistrationForms(request.POST or None)
    if request.method == "POST":
        post = form.save(commit=False)
        post.date_enrolled = timezone.now()
        student.update(student_level="Active")
        form.save()
    
    enrollment =  Enrollment.objects.filter(student = pk)
    
    if not enrollment:
        return render(request, 'registrar/student-profile.html', {'student': student})
    else:
        return render(request, 'registrar/student-profile.html', {'student': student, 'enrollment':enrollment, 'form': form})