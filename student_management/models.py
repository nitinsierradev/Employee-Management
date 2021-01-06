from django.db import models
from django.contrib.auth.models import User
import sys
# Create your models here.

class Project(models.Model):
    id                  = models.AutoField(primary_key=True)
    name                = models.CharField(max_length=100)
    is_active           = models.BooleanField(default=True)
    addedDate           = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='project'

class RankingCreteria(models.Model):
    id                  = models.AutoField(primary_key=True)
    rankingName         = models.CharField(max_length=200)
    is_active           = models.BooleanField(default=True)
    addedDate           = models.DateTimeField(auto_now_add=True)
    

    
    class Meta:
        db_table='ranking_creteria'

class Employee(models.Model):
    id                  = models.AutoField(primary_key=True)
    firstName           = models.CharField(max_length=200)
    lastName            = models.CharField(max_length=200)
    dob                 = models.DateField()
    email               = models.EmailField(max_length=200,unique=True)
    empId               = models.CharField(max_length=200)
    mobileNo            = models.CharField(max_length=10)
    photo               = models.ImageField(upload_to='emp-photo',null=True,blank=True)
    reportingEmployee   = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='employee_reporting')
    project             = models.ForeignKey(Project,on_delete=models.CASCADE)
    user                = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    addedDate           = models.DateTimeField(auto_now_add=True)
    is_active           = models.BooleanField(default=True)
    is_deleted          = models.IntegerField(default=0)

    class Meta:
        db_table='employee'
        unique_together=('empId','project')
        indexes = [
            models.Index(fields=['firstName'],name='firstName_idx'),
            models.Index(fields=['lastName'],name='lastName_idx')
        ]
    def __str__(self):
        return self.firstName


class EmployeeRating(models.Model):
    id                  = models.AutoField(primary_key=True)
    employee            = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='employee_rating')
    ratingCreteria      = models.ForeignKey(RankingCreteria,on_delete=models.CASCADE)
    rating              = models.IntegerField(default=0)


    class Meta:
        db_table ='employee_rating'

class EmployeeProjectLog(models.Model):
    id                  = models.AutoField(primary_key=True)
    employee            = models.ForeignKey(Employee,on_delete=models.CASCADE)
    project             = models.ForeignKey(Project,on_delete=models.CASCADE)
    added_date          = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='employee_project_log'








