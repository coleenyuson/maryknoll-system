from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

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
    students = Student.objects.all()
    return render(request, 'registrar/student-registration-list.html', {'student_list': students, 'form': form})

def studentDetails(request, pk='pk'):
    student = get_object_or_404(Student, pk=pk)
    '''form = RegistrationForms(request.POST or None)
    if request.method == "POST":
        post = form.save(commit=False)
        post.date_enrolled = timezone.now()
        form.save()
    '''
    enrollment =  Enrollment.objects.filter(student = pk)
    
    if not enrollment:
        return render(request, 'registrar/student-profile.html', {'student': student})
    else:
        return render(request, 'registrar/student-profile.html', {'student': student, 'enrollment':enrollment, 'form': form})

class StudentList(LoginRequiredMixin,generic.CreateView):
    #Create View and forms
    fields = ['first_name', 'last_name', 'status', 'birthplace','birthdate','home_addr',
            'postal_addr', 'm_firstname','m_middlename','m_lastname','m_occcupation',
            'f_firstname','f_middlename','f_lastname','f_occcupation','guardian']
    #Authentication
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    
    #Model used by this list view
    model = Student
    #PAGINATION, JUST ADD THIS VARIABLE AND ITS VALUE (check out the updated base_generic.html too!)
    #paginate_by = 5
    
    #Context name, used in the template handlebars
    #context_object_name = 'student_list'
    
    #Template name of this view
    template_name = 'registrar/student-list.html'
    
    def get_context_data(self, **kwargs):
        context = super(StudentList, self).get_context_data(**kwargs)
        context["student_list"] = self.model.objects.all()
        return context
    
class AddStudent(generic.CreateView):
    model = Student
    fields = []
    
def deets(request):
    return render(request, 'registrar/student-profile.html')