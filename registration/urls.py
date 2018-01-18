from django.conf.urls import url, include

from . import views

urlpatterns = [
        url(r'^$', views.index, name = 'reg-index'),
        url(r'^student-list/$', views.registrationList, name = 'student-list'),
        url(r'^student-list/(?P<pk>\d+)$', views.studentDetails, name = 'student-details'),
    ]