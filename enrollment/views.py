from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import *
from registration.models import *
from django.db.models import Q

#Local Functions -- Only for this module#
def initializeSchoolYear():
    '''PSEUDO CODE FOR INITIALIZATION'''
    #Create school year name with "S.Y." This Year, and This Year++
    #Year start date with THIS YEAR
    curr_year = datetime.today().year
    name = "S.Y. %s - %s" % (str(curr_year), str(curr_year+1))
    new_sy = School_Year.objects.create(year_name=name)
    new_sy.save()
#Local Functions -- End#

@login_required
def index(request):
    pass
#--------------------------------------CURRICULUM------------------------------------------------------
@login_required
def curriculumList(request):
    '''simple error handling: if current year is == year of latest curriculum created, disable the button'''

    try:
        latest_curr = Curriculum.objects.latest('curriculum_year')
    
        if datetime.today().year == latest_curr.get_year():
            disabled = True
    except:
        latest_curr = None
        disabled = False
    #redirect to new page
    return render(request, 'enrollment/curriculum-list.html', context={'disabled':disabled})

def addCurriculumProfile(request):
    #add constraints here
    new_curriculum = Curriculum(curriculum_status='Active')
    new_curriculum.save()
    return render(request, 'enrollment/curriculum-list.html')
    
def openCurriculumSubjectAdd(request, pk='pk'):
    curriculum = Curriculum.objects.get(curriculum_ID=pk)
    return render(request, 'enrollment/curriculum-list-add.html', {'curriculum':curriculum})

#--------------------------------------SCHOLARSHIP----------------------------------------------------
@login_required
def scholarshipList(request):
    return render(request, 'enrollment/scholarship-list.html')

def addScholarshipProfile(request):
    return render(request, 'enrollment/scholarship-list-add.html')
#--------------------------------------SUBJECT OFFERING------------------------------------------------
@login_required
def subjectOfferingList(request, pk='pk'):
    curr_sy = get_object_or_404(School_Year, id=pk)
    #Get current year
    curr_year = datetime.today().year
    #Get latest school year and check if you can create a new school year, and if its next or not
    #Change next and previous into objects --Jim
    pre_year = None
    next_year = None
    try:
        
        latest = School_Year.objects.latest('date_start')
        #next and previous
        oldest_sy = School_Year.objects.all().order_by('date_start').last()
        if curr_year < latest.get_year():
            disabled = False
        else:
            disabled = True
        if latest == curr_sy:
            next_year = None
        else:
            next_year = School_Year.objects.get(id=(pk+1))
        if str(curr_sy) == str(oldest_sy):
            pre_year = None
        else:
            pre_year = School_Year.objects.get(id=(pk-1))
    except:
        pass
    context = {'pre_year': pre_year,
                'next_year': next_year, 
                'disabled': disabled, 
                'school_year':curr_sy,
            }
    return render(request, 'enrollment/subject-offering.html', context)
def newSchoolYear(request):
    initializeSchoolYear()
    school_year = School_Year.objects.latest('date_start')
    #redirect page to list

def addSubjectOfferingProfile(request, pk):
    school_year = School_Year.objects.get(id=pk)
    return render(request, 'enrollment/subject-offering-add.html', context= {'school_year':school_year})

#AJAX VIEWS --------------------------------------------------------------------
from django.template.loader import render_to_string
from django.http import JsonResponse
#--------------------------------------CURRICULUM------------------------------------------------------
def tableCurriculumList(request):
    curriculum_list = Curriculum.objects.all()
    #Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(curriculum_list, 10)
    
    try:
        curriculum = paginator.page(page)
    except PageNotAnInteger:
        curriculum = paginator.page(1)
    except EmptyPage:
        curriculum = paginator.page(paginator.num_pages)
        
    context = {'curriculum_list': curriculum}
    html_form = render_to_string('enrollment/table-curriculum-list.html',
        context,
        request = request,
    )
    return JsonResponse({'html_form' : html_form})

def createCurriculumProfile(request, pk):
    curr = Curriculum.objects.get(curriculum_ID = pk)
    data = {'form_is_valid' : False }

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.curriculum = curr
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = SubjectForm()
    context = {'form': form, 'curriculum':curr}
    data['html_form'] = render_to_string('enrollment/forms-curriculum-subjects-list-create.html',
        context,
        request=request,
    )
    return JsonResponse(data)
    
def curriculumDetails(request, pk='pk'):
    curriculum = get_object_or_404(Curriculum, curriculum_ID=pk)
    try:
        last_record = Subjects.objects.filter(curriculum=curriculum).latest('enrollment_ID')
    except:
        last_record = Subjects.objects.filter(curriculum=curriculum)
    return render(request, 'enrollment/curriculum-subjects-list.html', {'curriculum': curriculum, 'record':last_record})
    
def tableCurriculumSubjectList(request, pk='pk'):
    curriculum = get_object_or_404(Curriculum, curriculum_ID=pk)
    subject_list = Subjects.objects.filter(curriculum = curriculum)
    #Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(subject_list, 4)
    
    try:
        subject = paginator.page(page)
    except PageNotAnInteger:
        subject = paginator.page(1)
    except EmptyPage:
        subject = paginator.page(paginator.num_pages)
        
    context = {'subject_list': subject_list}
    html_form = render_to_string('enrollment/table-curriculum-subject-list.html',
        context,
        request = request,
    )
    
    data = {'html_form' : html_form}
    return JsonResponse(data)
    
def updateCurriculum(request, pk='pk'):
    instance = get_object_or_404(Curriculum, pk=pk)
    return render(request, 'enrollment/curriculum-list-update.html', {'instance': instance})


def editCurriculumForm(request, pk='pk'):
    instance = get_object_or_404(Curriculum, pk=pk)
    data = {'form_is_valid' : False }
    try:
        last_curriculum = Curriculum.objects.latest('curriculum_ID')
    except:
        last_curriculum = None
    if request.method == 'POST':
        form = CurriculumForms(request.POST, instance = instance)
        if form.is_valid():
            instance = form.save()
            instance.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = CurriculumForms(instance = instance)
    context = {'form': form, 'curriculum':last_curriculum, 'instance': instance}
    data['html_form'] = render_to_string('enrollment/forms-curriculum-edit.html',
        context,
        request=request,
    )
    return JsonResponse(data)
#--------------------------------------SECTION--------------------------------------------------------
def sectionList(request):
    return render(request,'enrollment/section-list.html')
    
def addSection(request):
    return render(request, 'enrollment/section-details-add.html')
    
def sectionDetails(request, pk='pk'):
    section = get_object_or_404(Section, pk=pk)
    return render(request, 'enrollment/section-details.html', {'section': section})
    
def sectionTable(request):
    section_list = getSectionList(request)
    print section_list
    #Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(section_list, 3)
    
    try:
        section = paginator.page(page)
    except PageNotAnInteger:
        section = paginator.page(1)
    except EmptyPage:
        section = paginator.page(paginator.num_pages)
        
    context = {'section_list': section}
    html_form = render_to_string('enrollment/table-section-list.html',
        context,
        request = request,
    )
    return JsonResponse({'html_form' : html_form})
    
def tableSectionDetail(request, pk='pk'):
    section = get_object_or_404(Section, pk=pk)
    
    section_enrollee_list = Enrollment.objects.filter(section = section)
    #Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(section_enrollee_list, 1)
    
    try:
        section_page = paginator.page(page)
    except PageNotAnInteger:
        sectio_page  = paginator.page(1)
    except EmptyPage:
        section_page = paginator.page(paginator.num_pages)
        
    context = {'section_enrollee_list': section_page}
    html_form = render_to_string('enrollment/table-section-details.html',
        context,
        request = request,
    )
    return JsonResponse({'html_form' : html_form})

def sectionDetailAdd(request, pk='pk'):
    instance = get_object_or_404(Section, pk=pk)
    return render(request, 'enrollment/section-details-add.html', {'instance': instance})

def sectionDetailForm(request, pk='pk'):
    data = {'form_is_valid' : True }
    section = get_object_or_404(Section, pk=pk)
    section_enrollee = Section_Enrollee.objects.filter(section = section)
    try:
        enrollment = Enrollment.objects.latest('enrollment_ID').filter(r)
    except:
        enrollment = None
        
    '''if request.method == 'POST':
        form = SectionForms(request.POST)
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
        form = SectionForms()'''
        
    context = {'last_record':enrollment, 'instance': instance}
    data['html_form'] = render_to_string('enrollment/forms-section-detail-create.html',
        context,
        request=request,
    )
    return JsonResponse(data)

def getSectionList(request):
    search = request.GET.get('search')
    genre = request.GET.get('genre')
    isNum = True
    try:
        int(search)
    except:
        isNum = False
    if(request.GET.get('search')!= "None"):
        if( (genre == "None" or genre == "All Categories") and isNum):
            query = Section.objects.filter(
                Q(section_ID__contains=search)|
                Q(section_name__icontains=search)|
                Q(section_capacity__contains=search)|
                Q(adviser__icontains=search)|
                Q(room__icontains=search)
            )
        if(genre == "None" or genre == "All categories"):
            query = Section.objects.filter(
                Q(section_ID__contains=search)|
                Q(section_name__icontains=search)|
                Q(section_capacity__contains=search)|
                Q(adviser__icontains=search)|
                Q(room__icontains=search)
            )
        elif(genre == "Section ID"):
            print "id"
            query = Section.objects.filter(section_ID__contains=search)
        elif(genre == "Section Name"):
            query = Section.objects.filter(section_name__icontains=search)
        elif(genre == "Room"):
            query = Section.objects.filter(room__icontains=search)
        elif(genre == "Adviser"):
            query = Section.objects.filter(adviser__icontains=search)
        else:
            print "wala"
            query = Section.objects.all() 
            
    else:
        return []
    return query
    
#AJAX VIEWS --------------------------------------------------------------------

def generateSectionForm(request):
    data = {'form_is_valid' : False }
    try:
        last_section = Section.objects.latest('section_ID')
    except:
        last_section = None
    if request.method == 'POST':
        form = SectionForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.section_status = 'a'
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = SectionForms()
    context = {'forms': form, 'section':last_section}
    print(form.is_valid())
    print(form.errors)
    data['html_form'] = render_to_string('enrollment/forms-section-create.html',
        context,
        request=request,
    )
    return JsonResponse(data)
    
#--------------------------------------SCHOLARSHIP----------------------------------------------------
def tableScholarshipList(request):
    scholarship_list = getScholarshipList(request)
    #Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(scholarship_list, 5)
    
    try:
        scholarship = paginator.page(page)
    except PageNotAnInteger:
        scholarship = paginator.page(1)
    except EmptyPage:
        scholarship = paginator.page(paginator.num_pages)
        
    context = {'scholarship_list': scholarship}
    html_form = render_to_string('enrollment/table-scholarship-list.html',
        context,
        request = request,
    )
    return JsonResponse({'html_form' : html_form})

def getScholarshipList(request):
    search = request.GET.get('search')
    genre = request.GET.get('genre')
    isNum = True
    try:
        int(search)
    except:
        isNum = False
    if(request.GET.get('search')!= "None"):
        if( (genre == "None" or genre == "All Categories") and isNum):
            query = Scholarship.objects.filter(
                Q(pk__contains=search)|
                Q(scholarship_name__icontains=search)|
                Q(school_year__contains=search)|
                Q(scholarship_type__icontains=search)
            )
        if(genre == "None" or genre == "All categories"):
            query = Scholarship.objects.filter(
                Q(pk__contains=search)|
                Q(scholarship_name__icontains=search)|
                Q(school_year__contains=search)|
                Q(scholarship_type__icontains=search)
            )
        elif(genre == "Scholarship ID"):
            print "id"
            query = Scholarship.objects.filter(pk__contains=search)
        elif(genre == "Scholarship Name"):
            query = Scholarship.objects.filter(scholarship_name__icontains=search)
        elif(genre == "Validity"):
            query = Scholarship.objects.filter(school_year__icontains=search)
        elif(genre == "Scholarship Type"):
            query = Scholarship.objects.filter(scholarship_type__icontains=search)
        else:
            print "wala"
            query = Scholarship.objects.all() 
            
    else:
        return []
    return query

def createScholarshipProfile(request):
    data = {'form_is_valid' : False }
    try:
        last_scholarship = Scholarship.objects.latest('scholarship_ID')
    except:
        last_scholarship = None
    if request.method == 'POST':
        form = ScholarshipForms(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            print form.errors
            data['form_is_valid'] = False
    else:
        form = ScholarshipForms()
    context = {'form': form, 'scholarship':last_scholarship}
    data['html_form'] = render_to_string('enrollment/forms-scholarship-create.html',
        context,
        request=request,
    )
    return JsonResponse(data)
    
def updateScholarship(request, pk='pk'):
    instance = get_object_or_404(Scholarship, pk=pk)
    return render(request, 'enrollment/scholarship-list-update.html', {'instance': instance})


def editScholarshipForm(request, pk='pk'):
    instance = get_object_or_404(Scholarship, pk=pk)
    data = {'form_is_valid' : False }
    try:
        last_scholarship = Scholarship.objects.latest('scholarship_ID')
    except:
        last_scholarship = None
    if request.method == 'POST':
        form = ScholarshipForms(request.POST, instance = instance)
        if form.is_valid():
            instance = form.save()
            instance.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = ScholarshipForms(instance = instance)
    context = {'form': form, 'scholarship':last_scholarship, 'instance': instance}
    data['html_form'] = render_to_string('enrollment/forms-scholarship-edit.html',
        context,
        request=request,
    )
    return JsonResponse(data)
    
#--------------------------------------SUBJECT OFFERING------------------------------------------------
def tableSubjectOfferingList(request, pk):
    sy = School_Year.objects.get(id=pk)
    subjectOffering_list = Offering.objects.filter(school_year = sy)
    #Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(subjectOffering_list, 10)
    
    try:
        subjectOffering = paginator.page(page)
    except PageNotAnInteger:
        subjectOffering = paginator.page(1)
    except EmptyPage:
        subjectOffering = paginator.page(paginator.num_pages)
        
    context = {'subjectOffering_list': subjectOffering}
    html_form = render_to_string('enrollment/table-subject-offering.html',
        context,
        request = request,
    )
    return JsonResponse({'html_form' : html_form})

def createSubjectOfferingProfile(request, pk):
    curr_sy = School_Year.objects.get(id=pk)
    data = {'form_is_valid' : False }
    try:
        last_subjectOffering = SubjectOffering.objects.latest('subjectOffering_ID')
    except:
        last_subjectOffering = None
    if request.method == 'POST':
        form = SubjectOfferingForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.school_year = curr_sy
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = SubjectOfferingForms()
    context = {'form': form, 'subjectOffering':last_subjectOffering, 'school_year': curr_sy}
    data['html_form'] = render_to_string('enrollment/forms-subject-offering-create.html',
        context,
        request=request,
    )
    return JsonResponse(data)
    
def subjectOfferingDetail(request, pk='pk'):
    subjOffering = get_object_or_404(Student, pk=pk)
    try:
        last_record = Enrollment.objects.filter(subjOffering=subjOffering).latest('enrollment_ID')
    except:
        last_record = Enrollment.objects.filter(subjOffering=subjOffering)
    return render(request, 'enrollment/subject-offering-add.html.html', {'subjOffering': subjOffering, 'record':last_record})
    


def updateSubjectOffering(request, pk='pk'):
    instance = get_object_or_404(Offering, pk=pk)
    return render(request, 'enrollment/subject-offering-update.html', {'instance': instance})


def editSubjectOfferingForm(request, pk='pk'):
    instance = get_object_or_404(Offering, pk=pk)
    data = {'form_is_valid' : False }
    try:
        last_subjectOffering = Offering.objects.latest('subjectOffering_ID')
    except:
        last_subjectOffering = None
    if request.method == 'POST':
        form = SubjectOfferingForms(request.POST, instance = instance)
        if form.is_valid():
            instance = form.save()
            instance.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = SubjectOfferingForms(instance = instance)
    context = {'form': form, 'subjectOffering':last_subjectOffering, 'instance': instance}
    data['html_form'] = render_to_string('enrollment/forms-subject-offering-edit.html',
        context,
        request=request,
    )
    return JsonResponse(data)
