from django.db import models


# Create your models here.

class bankData(models.Model):

    IFSC = models.CharField(max_length=100)
    bank_id = models.CharField(max_length=400)
    branch = models.CharField(max_length=400, blank=True, null=True)
    address = models.CharField(max_length=400, blank=True, null=True)
    city = models.CharField(max_length=400, blank=True, null=True)
    district = models.CharField(max_length=500, blank=True, null=True)
    state = models.CharField(max_length=500, blank=True, null=True)
    bank_name = models.CharField(max_length=500, blank=True, null=True)

