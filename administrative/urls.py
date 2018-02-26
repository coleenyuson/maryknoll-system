from django.conf.urls import url, include

from . import views

urlpatterns = [
        url(r'^$', views.index, name = 'reg-index'),
        url(r'^employee-list/$', views.userList, name = 'employee-list'),
        url(r'^employee-list/table$', views.tableEmployeeList, name = 'employee-table'),
        url(r'^employee-list/add$', views.addEmployeeProfile, name = 'employee-add'),
        url(r'^employee-list/create$', views.createEmployeeProfile, name = 'employee-create'),
        
    ]