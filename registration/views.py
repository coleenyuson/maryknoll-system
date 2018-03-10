from django.shortcuts import render, get_object_or_404
from django.views import generic

from django.utils import timezone
from datetime import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q

from .models import *
from .forms import StudentForms, RegistrationForms

from django.template.loader import render_to_string
from django.http import JsonResponse

from django.db import models
from django.http import StreamingHttpResponse
from django.views.generic import View
import csv

# Global Functions - can be applied anywhere
# EXPORT TO CSV class is at the bottom-most part of this code
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
def ajaxTable(request, template, context, data = None):
    # For templates that needs ajax
    html_form = render_to_string(template,
        context,
        request = request,
    )
    if data:
        data['html_form'] = html_form
    else:
        data = {'html_form' : html_form}
    return JsonResponse(data)
def getLatest(model, attribute, foreign_key = None, ref_attribute = None):
    if(foreign_key == None or ref_attribute == None):
        # Get latest record of a model, basing on a certain attribute
        # Returns an instance
        try:
            latest = model.objects.latest(attribute)
        except:
            latest = None
    else:
        # Get latest record of a model, basing on a certain attribute
        # Returns an instance. This is for models with Foreign Keys
        try:
            latest = model.objects.filter(ref_attribute=foreign_key).latest(attribute)
        except:
            latest = model.objects.filter(ref_attribute=foreign_key)
    return latest
def updateInstance(request, modelForm, instance):
    if request.method == 'POST':
        form = modelForm(request.POST, instance = instance)
        if form.is_valid():
            instance = form.save()
            instance.save()
    else:
        form = modelForm(instance = instance)
    return form
# Custom Functions - Only for this module

def getStudentList(request):
    # Get student list with filters IF there is any, if none, then return all
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
            query = Student.objects.filter(
                Q(first_name__contains=search)|
                Q(last_name__contains=search)|
                Q(middle_name__contains=search)|
                Q(student_level__contains=search)
            )
        elif(genre == "Student ID" and isNum):
            query = Student.objects.filter(student_ID=search)
        elif(genre == "Year/Level"):
            # This needs debugging. ex. JUNIOR_HIGH == 'j' but input is "Junior High"
            query = Student.objects.filter(student_level=search)
        else:
            print "wala"
            query = Student.objects.all() 
            
    else:
        return []
    return query
def verifyActive():
    # Get latest school year, then get the student's latest registration school_year
    # If they are equal, he is in this school year, == He is active 
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

# Views

def studentList(request):
    # Table view - table_StudentList
    return render(request, 'registrar/student-registration-list.html')
def table_StudentList(request):
    verifyActive()
    
    student_list = getStudentList(request)

    limited_students = paginateThis(request, student_list, 10)

    context = {'student_list': limited_students}

    template = 'registrar/table-student-list.html'

    return ajaxTable(request, template, context)

def addStudent(request):
    # Form view - form_addStudent
    return render(request, 'registrar/student-registration-list-add.html')
def form_addStudent(request):
    data = {'form_is_valid' : False }

    if request.method == 'POST':
        form = StudentForms(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = StudentForms()

    last_student = getLatest(Student, 'student_ID')
    context = {'form': form, 'student':last_student}
    template = 'registrar/forms-student-create.html'

    return ajaxTable(request, template, context, data)


def studentDetails(request, pk='pk'):
    current_student = get_object_or_404(Student, pk=pk)
    last_record = getLatest(Enrollment, 'enrollment_ID', current_student, Enrollment.student)
    return render(request, 'registrar/student-profile.html', {'student': current_student, 'record':last_record})
def table_studentDetails(request, pk='pk'):
    student = get_object_or_404(Student, pk=pk)
    enrollment_list = Enrollment.objects.filter(student = student)
    enrollment = paginateThis(request, enrollment_list, 10)

    context = {'enrollment_list': enrollment}
    
    template = 'registrar/table-student-profile.html'

    return ajaxTable(request, template, context)

def addEnrollment(request, pk='pk'):
    student = Student.objects.get(student_ID = pk)
    return render(request, 'registrar/student-profile-add.html', {'student': student})
def form_addEnrollment(request, pk='pk'):
    data = {'form_is_valid' : False }

    current_student = get_object_or_404(Student, pk=pk)
    enrollment = getLatest(Enrollment, 'enrollment_ID')

    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date_enrolled = datetime.now()
            post.student = Student.objects.get(student_ID = pk)
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
    template = 'registrar/forms-registration-create.html'

    return ajaxTable(request,template,context,data)

def updateStudentProfile(request, pk='pk'):
    instance = get_object_or_404(Student, pk=pk)
    return render(request, 'registrar/student-registration-list-update.html', {'instance': instance})
def form_updateStudentProfile(request, pk='pk'):
    instance = get_object_or_404(Student, pk=pk)
    data = {'form_is_valid' : False }
    last_student = getLatest(Student,'student_ID')

    form = updateInstance(request, StudentForms, instance)

    if form.is_valid():
        data['form_is_valid'] = True
    else:
        data['form_is_valid'] = False

    context = {'form': form, 'student':last_student, 'instance': instance}
    template = 'registrar/forms-student-edit.html'
    return ajaxTable(request,template,context,data)

def generateStudentCode(student):
    pass


''' EXPORTING TO CSV '''
#Call the second class.as_view() to generate CSV
class Echo(object):
    """An object that implements just the write method of the file-like interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value
class Export_Model_To_CSV(View):
    def get(self, request, *args, **kwargs):
        query = Student.objects.all()
        file_name = 'all_Students.csv'
        model = query.model
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
            (writer.writerow(row) for row in stream(headers, query)),
            content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="' +file_name+'"'
        return response
        
