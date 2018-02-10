from django.shortcuts import render
from .models import *
from .forms import *
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

#STATIC VIEWS ------------------------------------------------------------------
def sectionList(request):
    section_list = Section.objects.all()
    context = {
        'section_list' : section_list
    }
    return render(request,'enrollment/section-list.html', context)
    
def addSection(request):
    return render(request, 'enrollment/section-details-add.html')
    
def sectionDetails(request, pk='pk'):
    section = get_object_or_404(Section, pk=pk)
    
    return render(request, 'enrollment/student-details.html', {'section': section})
    
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
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = SectionForms()
    context = {'form': form, 'section':last_section}
    print form
    data['html_form'] = render_to_string('enrollment/forms-section-create.html',
        context,
        request=request,
    )
    return JsonResponse(data)