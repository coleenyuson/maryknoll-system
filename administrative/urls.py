from django.conf.urls import patterns, url
from django.contrib import admin
from administrative import views

urlpatterns = [
    url(r'^emp-list/', views.EmployeeList.as_view() , name = "emp-list"),
    url(r'^create-emp/$', views.EmployeeCreate.as_view(), name = 'emp-create'),
    url(r'^edit-emp/(?P<id>\d+)', views.EmployeeUpdate.as_view(), name = 'emp-edit'),
    url(r'^delete-emp/(?P<id>\d+)', views.EmployeeDelete.as_view(), name = 'emp-delete'),

]