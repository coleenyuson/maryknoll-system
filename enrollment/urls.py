from django.conf.urls import url, include

from . import views

urlpatterns = [
        url(r'^section/list/details$', views.sectionDetails, name = 'section-details'),
        url(r'^$', views.index, name = 'reg-index'),
        #-----------------------CURRICULUM---------------------------------------------------------
        url(r'^curriculum-list/$', views.curriculumList, name = 'curriculum-list'),
        url(r'^curriculum-list/table$', views.tableCurriculumList, name = 'curriculum-table'),
        url(r'^curriculum-list/add$', views.addCurriculumProfile, name = 'curriculum-add'),
        url(r'^curriculum-list/create$', views.createCurriculumProfile, name = 'curriculum-create'),
        url(r'^curriculum-list/update/(?P<pk>\d+)$', views.updateCurriculum, name = 'curriculum-update'),
        url(r'^curriculum-list/edit-form/(?P<pk>\d+)$', views.editCurriculumForm, name = 'curriculum-edit-form'),
        #CURR DETAIL
        url(r'^curriculum-list/(?P<pk>\d+)/$', views.curriculumDetails, name = 'curriculum-detail'),
        url(r'^curriculum-list/subject-table/(?P<pk>\d+)$', views.tableCurriculumSubjectList, name = 'subject-table'),
        #-----------------------SECTION------------------------------------------------------------
        url(r'^section-list$', views.sectionList, name = 'section-list'),
        url(r'^section-list/table$', views.sectionTable, name = 'section-table'),
        url(r'^section-list/add$', views.addSection, name = 'section-create'),
        
        url(r'^section-list/add-form$', views.generateSectionForm, name = 'section-create-form'),
        url(r'^section-list/(?P<pk>\d+)/$', views.sectionDetails, name = 'section-detail'),
        url(r'^section-list/detail-table/(?P<pk>\d+)$', views.tableSectionDetail, name = 'section-detail-table'),
        
        url(r'^section-list/section-detail-add/(?P<pk>\d+)$', views.sectionDetailAdd, name = 'section-detail-add'),
        url(r'^section-list/section-detail-form/(?P<pk>\d+)$', views.sectionDetailForm, name = 'section-detail-form'),
        
        #-----------------------SCHOLARSHIP--------------------------------------------------------
        url(r'^scholarship-list/$', views.scholarshipList, name = 'scholarship-list'),
        url(r'^scholarship-list/table$', views.tableScholarshipList, name = 'scholarship-table'),
        url(r'^scholarship-list/add$', views.addScholarshipProfile, name = 'scholarship-add'),
        url(r'^scholarship-list/create$', views.createScholarshipProfile, name = 'scholarship-create'),
        
        url(r'^scholarship-list/update/(?P<pk>\d+)$', views.updateScholarship, name = 'scholarship-update'),
        url(r'^scholarship-list/edit-form/(?P<pk>\d+)$', views.editScholarshipForm, name = 'scholarship-edit-form'),
        #-----------------------SUBJECT OFFERING----------------------------------------------------
        url(r'^subjectOffering-list/$', views.subjectOfferingList, name = 'subjectOffering-list'),
        url(r'^subjectOffering-list/table$', views.tableSubjectOfferingList, name = 'subjectOffering-table'),
        url(r'^subjectOffering-list/add$', views.addSubjectOfferingProfile, name = 'subjectOffering-add'),
        url(r'^subjectOffering-list/create$', views.createSubjectOfferingProfile, name = 'subjectOffering-create'),
        url(r'^subjectOffering-list/(?P<pk>\d+)/$', views.subjectOfferingDetail, name = 'subjectOffering-detail'),
        
        url(r'^subjectOffering-list/update/(?P<pk>\d+)$', views.updateSubjectOffering, name = 'subjectOffering-update'),
        url(r'^subjectOffering-list/edit-form/(?P<pk>\d+)$', views.editSubjectOfferingForm, name = 'subjectOffering-edit-form'),
    ]