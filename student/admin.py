from django.contrib import admin
from .models import Student, AssignmentSubmission, Attendance

# Register your models here.

admin.site.register(Student)
admin.site.register(AssignmentSubmission)
admin.site.register(Attendance)
