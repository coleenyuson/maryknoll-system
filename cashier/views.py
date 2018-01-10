from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import FeesAccounts

class FAList(ListView):
    model = FeesAccounts
    context_object_name = 'fees_accounts'
    template_name = '/cashier/fa_list.html'

class FACreate(CreateView):
    model = FeesAccounts
    pk_url_kwarg = "id"
    success_url = reverse_lazy('fa-list')
    fields = ['fa_name', 'amount']
    template_name = '/cashier/fa_form.html'

class FAUpdate(UpdateView):
    model = FeesAccounts
    pk_url_kwarg = "id"
    success_url = reverse_lazy('fa-list')
    fields = ['fa_name', 'amount']
    template_name = '/cashier/fa_form.html'

class FADelete(DeleteView):
    model = FeesAccounts
    pk_url_kwarg = "id"
    success_url = reverse_lazy('fa-list')
    template_name = '/cashier/fa_confirm_delete.html'