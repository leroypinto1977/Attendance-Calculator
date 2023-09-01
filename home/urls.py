from django.contrib import admin
from django.urls import path, include
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
  path('attendance_calc', views.attendance, name = "attendance"),
  path('course_details', views.course_details, name = "course_details"),
  path('subject_details', views.subject_details, name = "subject_details"),
  path('enter_attendance', views.enter_attendance, name = "enter_attendance"),
  path('settings', views.settings, name = "settings"),
]
