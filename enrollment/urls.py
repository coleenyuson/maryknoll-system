from django.conf.urls import url, include

from . import views

urlpatterns = [
        url(r'^section-list/$', views.sectionList, name = 'section-list'),
    ]