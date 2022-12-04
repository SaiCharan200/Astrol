from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("login", views.login, name='login'),
    path("register", views.register, name='register'),
    path('logout', views.user_logout, name='logout'),
    path("freereports", views.freereports, name='freereports'),
    path("Report", views.Report, name='Report'),
    path("trait", views.trait, name='trait'),
    path("rashi", views.rashi, name='rashi'),
    path("learnastro", views.learnastro, name='learnastro'),
    path("numerology", views.numerology, name='numerology'),
    path("Birthdate", views.Birthdate, name='Birthdate'),
    path("Numerologynumbers", views.Numerologynumbers, name='Numerologynumbers'),
    path("career", views.career, name='career'),
    path("feedback", views.feedback, name='feedback'),

]
