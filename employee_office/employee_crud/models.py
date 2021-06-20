from django.db import models

class EmployeeDetails(models.Model):

    name = models.CharField(max_length=30)
    eid = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)
    salary = models.IntegerField(default=15000)
    mobno = models.CharField(max_length=12)
    address = models.CharField(max_length=25)

    def __str__(self):
        return self.name


