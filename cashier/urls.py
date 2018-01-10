from django.conf.urls import url
from django.contrib import admin
from cashier import views

urlpatterns = [
    url(r'^fa-list/', views.FAList.as_view() , name = "fa-list"),
    url(r'^create-fa/$', views.FACreate.as_view(), name = 'fa-create'),
    url(r'^edit-fa/(?P<id>\d+)', views.FAUpdate.as_view(), name = 'fa-edit'),
    url(r'^delete-fa/(?P<id>\d+)', views.FADelete.as_view(), name = 'fa-delete'),

]