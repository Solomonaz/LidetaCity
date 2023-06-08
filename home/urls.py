from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feedback/', views.feedback, name='feedback'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('gallery/', views.gallery, name='gallery'),
    path('chiefexecutive/', views.chiefexecutive, name='chiefexecutive'),
    path('cabinate/', views.cabinate, name='cabinate'),
    path('woredas/', views.woredas, name='woredas'),
    path('structure/', views.structure, name='structure'),
    path('offices/', views.offices, name='offices'),
    path('woredas/', views.woredas, name='woredas'),

    path('tender/', views.tender, name='tender'),
    path('vacancy/', views.vacancy, name='vacancy'),
    path('event/', views.event, name='event'),

]
