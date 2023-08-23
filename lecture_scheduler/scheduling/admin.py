from django.contrib import admin
from .models import Instructor, Course, Lecture, Account
from .forms import InstructorForm



admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Account)