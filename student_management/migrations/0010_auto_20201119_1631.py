# Generated by Django 2.2.12 on 2020-11-19 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management', '0009_auto_20201112_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='reportingEmployee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_reporting', to='student_management.Employee'),
        ),
    ]
