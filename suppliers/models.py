from django.db import models

class Currency(models.Model):
    currency_name = models.CharField(max_length=100)
    currency_symbol = models.CharField(max_length=3)

    class Meta: 
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

    def __str__(self):
        return f'{self.currency_name} {self.currency_symbol}'
    

class Rate(models.Model):
    currency_name = models.CharField(max_length=100)
    currency_rate = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.currency_name} = {self.currency_rate}LBP'



class Supplier(models.Model):
    supplier_name = models.CharField(max_length=200)
    supplier_phone = models.CharField(max_length=200)
    supplier_address = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    notes = models.TextField()

    def __str__(self):
        return str(self.supplier_name)

class ContactPerson(models.Model):
    company = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    contact_name = models.CharField(max_length=200, null=True, blank=True)
    contact_mobile = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    Job_title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return str(self.contact_name)


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    dealer_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    product_description = models.TextField()

    def __str__(self):
        return self.product_name




# person2 = ContactPerson.objects.filter(company__supplier_name="pcdealnet")
