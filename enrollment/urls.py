from django.conf.urls import url
from django.contrib import admin
from enrollment import views

urlpatterns = [
    url(r'^section-list/', views.SectionList.as_view() , name = "section-list"),
    url(r'^create-section/$', views.SectionCreate.as_view(), name = 'section-create'),
    url(r'^edit-section/(?P<id>\d+)', views.SectionUpdate.as_view(), name = 'section-edit'),
    url(r'^delete-section/(?P<id>\d+)', views.SectionDelete.as_view(), name = 'section-delete'),
    
    url(r'^shsSubj-list', views.SHS_SubjList.as_view() , name = "shsSubj-list"),
    url(r'^create-shsSubj/$', views.SHS_SubjCreate.as_view(), name = 'shsSubj-create'),
    url(r'^edit-shsSubj/(?P<id>\d+)', views.SHS_SubjUpdate.as_view(), name = 'shsSubj-edit'),
    url(r'^delete-shsSubj/(?P<id>\d+)', views.SHS_SubjDelete.as_view(), name = 'shsSubj-delete'),

]