from django.contrib import admin
from django.urls import path, include
from home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name ='home'),
    path('login',views.loginUser, name='login'),
    path('logout',views.logout_user, name='logout'),
    path('sign',views.sign, name='sign'),
    path('ajax',views.ajax, name='ajax'),
    path('input',views.input, name='input'),
    path('urlGod',views.urlGod, name='urlGod'),
    path('php',views.php, name='php'),
    path('urlLord',views.urlLord, name='urlLord'),
    path('number',views.get_number, name='number'),
    path('base',views.base, name='base'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup", views.authview, name = 'authview'),
    path("log", views.logview, name = 'logview'),
    path('teacherLog', views.teacher_login, name = 'teacher_login'),  
    path('teacherReg', views.teacher_registration, name = 'teacher_registration'),
    path('teacher_page',views.teacherPage, name='teacher_page'),
    path('qr_generate',views.qr_generate, name='qr_generate'),
    path('send_subject', views.send_subject, name='send_subject'),
    path('presenty', views.presenty, name='presenty'),
    path('send_qr', views.send_qr, name='send_qr'),
    path('students', views.student_list, name='student_list'),
    path('option',views.option, name='option'),
    path('get',views.get, name='get')
]


