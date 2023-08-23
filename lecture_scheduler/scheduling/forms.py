# scheduling/forms.py

from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import Course, Lecture,Account, Instructor

class InstructorForm(UserCreationForm):
    class Meta:
        model = Instructor
        fields = ['name', 'email']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'level', 'description', 'image', 'instructor']

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['course', 'instructor', 'date']


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={
    'placeholder': 'Enter the password',
    'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={
    'placeholder': 'Confirm password',
    'class': 'form-control',
    }))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email']
