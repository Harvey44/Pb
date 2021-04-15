from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Customprofile(AbstractUser):
    balance = models.CharField(max_length=2000)
    figure = models.IntegerField(default=0)
    total_credit = models.CharField(max_length=2000)
    total_debit = models.CharField(max_length=2000)
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=15)
    pin = models.CharField(max_length=8)
    transfer_code = models.CharField(max_length=8)

    class Meta:
        verbose_name = "Custom Profile"
        verbose_name_plural = "Custom Profile"


class Transactions(models.Model):
    user = models.ForeignKey(Customprofile, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(default=0)
    reference = models.CharField(max_length=1000, blank=True)
    fullname = models.CharField(max_length=1000, blank=True)
    country = models.CharField(max_length=1000, blank=True)
    bankname = models.CharField(max_length=1000, blank=True)
    number = models.CharField(max_length=1000, blank=True)
    swift = models.CharField(max_length=1000, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Transactions"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return self.user.username