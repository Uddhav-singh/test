from django.shortcuts import render, redirect
from .models import Instructor, Course, Lecture
from .forms import CourseForm, LectureForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout


def home(request):
    return render(request, 'base.html')

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    
    return render(request, 'scheduling/add_course.html', {'form': form})

def assign_lecture(request):
    if request.method == 'POST':
        form = LectureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lecture_list')
    else:
        form = LectureForm()
    
    return render(request, 'scheduling/assign_lecture.html', {'form': form})

def instructor_assignments(request):
    instructor_id = request.user.id  # Assuming you're using user authentication
    lectures = Lecture.objects.filter(instructor=instructor_id)
    
    return render(request, 'scheduling/instructor_assignments.html', {'lectures': lectures})



# registeration and login/log-out views

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a suitable view after registration
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})




def user_login(request):
    if request.method == 'POST':
        # Implement login form processing here
        return redirect('home')  # Redirect to a suitable view after login
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to a suitable view after logout


