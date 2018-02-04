from django.conf.urls import url, include

from . import views

urlpatterns = [
        url(r'^$', views.index, name = 'reg-index'),
        url(r'^user-list/$', views.userList, name = 'employee-list'),
        url(r'^user-list/table$', views.tableEmployeeList, name = 'employee-table'),
    ]