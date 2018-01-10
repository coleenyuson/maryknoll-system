from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from enrollment.models import Sections, SHS_Subjects

class SectionList(ListView):
    model = Sections
    context_object_name = 'section'
    template_name = 'enrollment/section_list.html'

class SectionCreate(CreateView):
    model = Sections
    pk_url_kwarg = "id"
    success_url = reverse_lazy('section-list')
    fields = ['section_name', 'section_status']
    template_name = 'enrollment/section_form.html'

class SectionUpdate(UpdateView):
    model = Sections
    pk_url_kwarg = "id"
    success_url = reverse_lazy('section-list')
    fields = ['section_name', 'section_status']
    template_name = 'enrollment/section_form.html'

class SectionDelete(DeleteView):
    model = Sections
    pk_url_kwarg = "id"
    success_url = reverse_lazy('section-list')
    template_name = 'enrollment/section_confirm_delete.html'
    
    #----------------------------------------------------------
    
class SHS_SubjList(ListView):
    model = SHS_Subjects
    context_object_name = 'section-shs_subs'
    template_name = 'enrollment/shsSubj_list.html'

class SHS_SubjCreate(CreateView):
    model = SHS_Subjects
    pk_url_kwarg = "id"
    success_url = reverse_lazy('section-list')
    fields = ['s_subjectName', 's_desc', 's_status']
    template_name = 'enrollment/shsSubj_form.html'

class SHS_SubjUpdate(UpdateView):
    model = SHS_Subjects
    pk_url_kwarg = "id"
    success_url = reverse_lazy('section-list')
    fields = ['s_subjectName', 's_desc', 's_status']
    template_name = 'enrollment/shsSubj_form.html'

class SHS_SubjDelete(DeleteView):
    model = SHS_Subjects
    pk_url_kwarg = "id"
    success_url = reverse_lazy('section-list')
    template_name = 'enrollment/shsSubj_confirm_delete.html'