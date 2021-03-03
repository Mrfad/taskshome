from django.db import models
from django.contrib.auth.models import User
from suppliers.models import Currency
from users.models import Profile

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_first_name = models.CharField(max_length=200)
    customer_last_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    customer_address = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    notes = models.TextField()

    def __str__(self):
        return str(self.customer_first_name) + ' ' + str(self.customer_last_name)

class Account(models.Model):
    max_discount = models.DecimalField(max_digits=2, decimal_places=2)
    credit_limit = models.DecimalField(max_digits=20, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    sales_man = models.OneToOneField(User, on_delete=models.CASCADE)
    Agent = models.OneToOneField(Profile, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    reason = models.TextField()


