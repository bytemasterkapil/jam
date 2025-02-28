from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('jobseekerreg/',views.jobseekerreg,name='jobseekerreg'),
    path('employerreg/',views.employerreg,name='employerreg'),
    path('login/',views.login,name='login'),
    path('contact/',views.contact,name='contact'),
    path('jsreg/',views.jsreg,name='jsreg'),
    path('ereg/',views.ereg,name='ereg'),
    path('saveenq/',views.saveenq,name='saveenq'),
    path('validate/',views.validate,name='validate'),
    path('emphome/', views.emphome, name='emphome'),
    path('postjob/', views.postjob, name='postjob'),
    path('manageapp/', views.manageapp, name='manageapp'),
    path('empchangepassword/', views.empchangepassword, name='empchangepassword'),
    path('emplogout/', views.emplogout, name='emplogout'),
    path('pjob/', views.pjob, name='pjob'),
    path('empchangepwd/', views.empchangepwd, name='empchangepwd'),

]