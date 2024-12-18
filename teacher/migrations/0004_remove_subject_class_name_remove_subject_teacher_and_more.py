# Generated by Django 5.1.4 on 2024-12-13 06:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_alter_subject_class_name_alter_subject_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='class_name',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='teacher',
        ),
        migrations.CreateModel(
            name='TeachingAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='teacher.class')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='teacher.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='teacher.teacher')),
            ],
            options={
                'unique_together': {('teacher', 'subject', 'class_model')},
            },
        ),
    ]