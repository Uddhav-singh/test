# scheduling/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add_course/', views.add_course, name='add_course'),
    path('assign_lecture/', views.assign_lecture, name='assign_lecture'),
    path('instructor_assignments/', views.instructor_assignments, name='instructor_assignments'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

]
