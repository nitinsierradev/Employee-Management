from django.db import models
from student_management.models import Employee

class Challan(models.Model):
    officer             = models.ForeignKey(Employee,on_delete=models.CASCADE)
    plateNo             = models.CharField(max_length=200)
    driverLicenseNumber = models.CharField(max_length=200)
    penaltyAmount       = models.IntegerField(default=0)
    penaltyReason       = models.TextField()
    paidStatus          = models.BooleanField(default=False)
    addedDate           = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='challan'





