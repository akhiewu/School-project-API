# Generated by Django 4.0.1 on 2022-01-17 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='course',
            new_name='course_code',
        ),
    ]
