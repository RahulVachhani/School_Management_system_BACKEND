# Generated by Django 5.1.4 on 2024-12-12 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_class_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='class_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_name', to='teacher.class'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='code',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='class',
            unique_together={('name', 'section')},
        ),
    ]