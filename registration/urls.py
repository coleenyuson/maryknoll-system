from django.conf.urls import url, include

from . import views

urlpatterns = [
        url(r'^$', views.index, name = 'reg-index'),
        url(r'^student-list/$', views.studentList, name = 'student-list'),
        url(r'^student-list/download$', views.Export_Model_To_CSV.as_view(), name = 'student-list-download'), #new feature, delete this line if you have seen this already -aji
        url(r'^student-list/table$', views.table_StudentList, name = 'student-table'),
        url(r'^student-list/add$', views.addStudent, name = 'student-add'),
        url(r'^student-list/create$', views.form_addStudent, name = 'student-add-form'),
        url(r'^student-list/update/(?P<pk>\d+)$', views.updateStudentProfile, name = 'student-update'),
        url(r'^student-list/edit-form/(?P<pk>\d+)$', views.form_updateStudentProfile, name = 'student-edit-form'),
        #student profile urls
        url(r'^student-list/(?P<pk>\d+)$', views.studentDetails, name = 'student-details'),
        url(r'^student-list/enrollment-table/(?P<pk>\d+)$', views.table_studentDetails, name = 'enrollment-table'),
        url(r'^student-list/enrollment-add/(?P<pk>\d+)$', views.addEnrollment, name = 'enrollment-add'),
        url(r'^student-list/enrollment-create/(?P<pk>\d+)$', views.form_addEnrollment, name = 'enrollment-create'),
        #url(r'^student-list/enrollment-create/sort(?P<pk>\d+)$', views.sortSections, name = 'sort-sections'),
    ]