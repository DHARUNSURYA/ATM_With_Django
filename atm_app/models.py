from django.db import models

# Create your models here.


class Account(models.Model):
    account_number = models.CharField(max_length=10, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    pin = models.CharField(max_length=4) 

    def __str__(self):
        return self.account_number
