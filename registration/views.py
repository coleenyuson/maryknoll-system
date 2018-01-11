from django.shortcuts import render
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

from models import *

@login_required
def index(request):
    pass
    #return render(request,'/registration/index.html',)
    
class StudentList(LoginRequiredMixin,generic.ListView):
    #Authentication
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    
    #Model used by this list view
    model = Student
    
    #PAGINATION, JUST ADD THIS VARIABLE AND ITS VALUE (check out the updated base_generic.html too!)
    #paginate_by = 5
    
    #Context name, used in the template handlebars
    context_object_name = 'student_list'
    
    #Template name of this view
    template_name = 'registrar/student-list.html'
    
class AddStudent(generic.CreateView):
    model = Student
    fields = []
    