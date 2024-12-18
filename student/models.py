
from django.db import models
from django.conf import settings

from teacher.models import Class,Assignment

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student_profile", blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True, blank=True)
    enrollment_number = models.CharField(max_length=20, unique=True,blank=True,null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    class_name = models.ForeignKey(Class, on_delete=models.SET_NULL, related_name="students", blank=True,null=True)
    
    def __str__(self):
        return f"{self.first_name} - {self.enrollment_number}"
    

class AssignmentSubmission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    submitted_at = models.DateTimeField(auto_now_add=True)
    submission_file = models.FileField(upload_to='submissions/', null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('graded', 'Graded'), ('submitted', 'Submitted')],
        default='pending'
    )


    class Meta:
        unique_together = ('student', 'assignment')
        indexes = [
            models.Index(fields=['student']),
            models.Index(fields=['assignment']),
        ]

    # def clean(self):
    #     if self.submission_file and self.submission_file.size > 5 * 1024 * 1024:
    #         raise ValidationError("File size should not exceed 5 MB.")

    def __str__(self):
        return f"Submission for {self.assignment.title} by {self.student.user.username}"

    

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendances")
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="class_attendance")
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='absent')

    class Meta:
        unique_together = ('student', 'class_name', 'date')  
        ordering = ['-date']

    def __str__(self):
        return f"{self.student.first_name} - {self.class_name.name} ({self.date})"