from audioop import maxpp
from django.db import models
from django.contrib.auth.models import User as U
from django.contrib.auth.models import AbstractUser
# Create your models here.

class PayPlan(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(created_at=True)


class Users(AbstractUser):
    full_name = models.CharField(max_length=100, null=False)
    pay_plan = models.ForeignKey(PayPlan, on_delete=models.DO_NOTHING, null=True)
