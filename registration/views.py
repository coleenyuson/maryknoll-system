from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q
# Create your views here.
from .models import *
from .forms import StudentForms, RegistrationForms

#STATIC VIEWS ------------------------------------------------------------------
@login_required
def index(request):
    pass
    #return render(request,'/registration/index.html',)

@login_required
def registrationList(request):
    return render(request, 'registrar/student-registration-list.html')

def addStudentProfile(request):
    return render(request, 'registrar/student-registration-list-add.html')

@login_required
def studentDetails(request, pk='pk'):
    student = get_object_or_404(Student, pk=pk)
    try:
        last_record = Enrollment.objects.filter(student=student).latest('subject_ID')
    except:
        last_record = Enrollment.objects.filter(student=student)
    return render(request, 'registrar/student-profile.html', {'student': student, 'record':last_record})
    
def addEnrollment(request, pk = 'pk'):
    student = Student.objects.get(student_ID = pk)
    return render(request, 'registrar/student-profile-add.html', {'student': student})
#AJAX VIEWS --------------------------------------------------------------------
from django.template.loader import render_to_string
from django.http import JsonResponse

def searchStudent(request):
    search = request.GET.get('search', None)
    data = {
        'is_taken': Student.objects.filter(first_name__contains=search).exists()
    }
    return JsonResponse(data)
    
def getStudentList(request):
    search = request.GET.get('search')
    genre = request.GET.get('genre')
    isNum = True
    try:
        int(search)
    except:
        isNum = False
    if(request.GET.get('search')!= "None"):
        if( (genre == "None" or genre == "All Categories") and isNum):
            query = Student.objects.filter(
                Q(student_ID__contains=search)|
                Q(first_name__contains=search)|
                Q(last_name__contains=search)|
                Q(middle_name__contains=search)|
                Q(student_level__contains=search)
            )
        if(genre == "None" or genre == "All categories"):
            query = Student.objects.filter(
                Q(first_name__contains=search)|
                Q(last_name__contains=search)|
                Q(middle_name__contains=search)|
                Q(student_level__contains=search)
            )
        elif(genre == "Name"):
            print "name"
            query = Student.objects.filter(
                Q(first_name__contains=search)|
                Q(last_name__contains=search)|
                Q(middle_name__contains=search)|
                Q(student_level__contains=search)
            )
        elif(genre == "Student ID" and isNum):
            print "id"
            query = Student.objects.filter(student_ID=search)
        elif(genre == "Year/Level"):
            query = Student.objects.filter(student_level=search)
        else:
            print "wala"
            query = Student.objects.all() 
            
    else:
        return []
    return query

def tableStudentList(request):
    verifyActive()
    student_list = getStudentList(request)
    print student_list
    #Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(student_list, 10)
    
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)
    
    context = {'student_list': students}
    html_form = render_to_string('registrar/table-student-list.html',
        context,
        request = request,
    )
    return JsonResponse({'html_form' : html_form})

def createStudentProfile(request):
    data = {'form_is_valid' : False }
    try:
        last_student = Student.objects.latest('student_ID')
    except:
        last_student = None
    if request.method == 'POST':
        form = StudentForms(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = StudentForms()
    context = {'form': form, 'student':last_student}
    data['html_form'] = render_to_string('registrar/forms-student-create.html',
        context,
        request=request,
    )
    return JsonResponse(data)
    
def tableEnrollmentList(request, pk='pk'):
    student = get_object_or_404(Student, pk=pk)
    
    enrollment_list = Enrollment.objects.filter(student = student)
    #Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(enrollment_list, 4)
    
    try:
        enrollment = paginator.page(page)
    except PageNotAnInteger:
        enrollment = paginator.page(1)
    except EmptyPage:
        enrollment = paginator.page(paginator.num_pages)
        
    context = {'enrollment_list': enrollment}
    html_form = render_to_string('registrar/table-student-profile.html',
        context,
        request = request,
    )
    
    data = {'html_form' : html_form}
    return JsonResponse(data)

def createEnrollment(request, pk='pk'):
    data = {'form_is_valid' : False }
    current_student = get_object_or_404(Student, pk=pk)
    try:
        enrollment = Enrollment.objects.latest('enrollment_ID')
    except:
        enrollment = None
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        form.date_enrolled = datetime.now()
        form.student = Student.objects.get(student_ID = pk)
        if form.is_valid():
            post = form.save(commit=False)
            post.student_type='n'
            current_student.status="a"
            form.save()
            data['form_is_valid'] = True
        else:
            print form.errors
            data['form_is_valid'] = False
    else:
        form = RegistrationForms()
    context = {'form': form, 'student':current_student, 'last_record':enrollment}
    data['html_form'] = render_to_string('registrar/forms-registration-create.html',
        context,
        request=request,
    )
    return JsonResponse(data)
    
def verifyActive():
    student_list = Student.objects.all()
    for curr_student in student_list:
        try:
            last_record = Enrollment.objects.get(student=curr_student.student_ID)
        except:
            last_record = None
        try:
            curr_schoolyear = School_Year.objects.latest('year_name')
        except:
            curr_schoolyear = None
        if ((curr_schoolyear == None) or (last_record == None)):
            break
        elif (curr_schoolyear == last_record.school_year):
            curr_student.status = "a"
            curr_student.save()
            
      
      
#CUSTOM MADE FUNCTIONS -------------------------------------------------------------
def generateStudentCode(student):
    pass
#REPORTS -------------------------------------------------------------

from django.db import models
from django.http import StreamingHttpResponse
from django.views.generic import View
import csv
class Echo(object):
    """An object that implements just the write method of the file-like interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value
class ContactLogExportCsvView(View):
    def get(self, request, *args, **kwargs):
        student_query = Student.objects.all() # Assume 50,000 objects inside
        model = student_query.model
        model_fields = model._meta.fields + model._meta.many_to_many
        headers = [field.name for field in model_fields] # Create CSV headers
        def get_row(obj):
            row = []
            for field in model_fields:
                if type(field) == models.ForeignKey:
                    val = getattr(obj, field.name)
                    if val:
                        val = val.__unicode__()
                elif type(field) == models.ManyToManyField:
                    val = u', '.join([item.__unicode__() for item in getattr(obj, field.name).all()])
                elif field.choices:
                    val = getattr(obj, 'get_%s_display'%field.name)()
                else:
                    val = getattr(obj, field.name)
                row.append(unicode(val).encode("utf-8"))
            return row
        def stream(headers, data): # Helper function to inject headers
            if headers:
                yield headers
            for obj in data:
                yield get_row(obj)
        pseudo_buffer = Echo()
        writer = csv.writer(pseudo_buffer)
        response = StreamingHttpResponse(
            (writer.writerow(row) for row in stream(headers, student_query)),
            content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="all_Students.csv"'
        return response
        
        
