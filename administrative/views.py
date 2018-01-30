from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def employeeCreate(request):
    #data = {'form_is_valid' : False }
    try:
        last_employee = Employee.objects.latest('student_ID')
    except:
        last_employee = None
    if request.method == 'POST':
        form = EmployeeForms(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = EmployeeForms()
    context = {'form': form, 'employee':last_employee}
    '''data['html_form'] = render_to_string('registrar/partial-student-create.html',
        context,
        request=request,
    )
    return JsonResponse(data)'''
    
    return render(request, 'administrative/admin-employee.html', context)