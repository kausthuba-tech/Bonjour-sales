from django.db import models

# Create your models here.
class EMPLOYEE(models.Model):
    def __str__(self):
        return self.username
    username = models.CharField(max_length=100)
    shift = models.CharField(max_length=300)
    timings = models.IntegerField()
    salaryperday = models.IntegerField()

class STORES(models.Model):
    def __str__(self):
        return self.storename
    storename = models.CharField(max_length=100)
    Branch = models.CharField(max_length=300)

class ORDER(models.Model):
    def __str__(self):
        return self.ordername
    ordername = models.CharField(max_length=100)
    quantity = models.IntegerField()


