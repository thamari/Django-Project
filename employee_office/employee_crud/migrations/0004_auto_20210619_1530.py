# Generated by Django 3.2 on 2021-06-19 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_crud', '0003_rename_employee_details_employeedetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetails',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='employeedetails',
            name='start_date',
        ),
    ]
