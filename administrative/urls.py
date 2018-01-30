from django.conf.urls import url, include

from . import views

urlpatterns = [
        url(r'^employee-create/$', views.employeeCreate, name = 'employee-list'),
    ]