from django.conf.urls import url, include

from . import views

urlpatterns = [
        url(r'^section/list$', views.sectionList, name = 'section-list'),
        url(r'^section/list/add$', views.addSection, name = 'section-create'),
        url(r'^section/list/add-form$', views.generateSectionForm, name = 'section-create-form'),
        url(r'^section/list/details$', views.sectionDetails, name = 'section-details'),
    ]