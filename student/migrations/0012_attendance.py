# Generated by Django 5.1.4 on 2024-12-17 05:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_remove_student_class_name_student_class_name'),
        ('teacher', '0008_alter_assignment_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('present', 'Present'), ('absent', 'Absent')], default='absent', max_length=10)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_attendance', to='teacher.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='student.student')),
            ],
            options={
                'ordering': ['-date'],
                'unique_together': {('student', 'class_name', 'date')},
            },
        ),
    ]