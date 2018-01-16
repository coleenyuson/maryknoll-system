from django.conf.urls import url, include

from . import views

urlpatterns = [
        url(r'^$', views.index, name = 'reg-index'),
        url(r'^student-list', views.StudentList.as_view(), name = 'student-list'),
        url(r'^student-details', views.deets, name = 'student-details'),
    ]