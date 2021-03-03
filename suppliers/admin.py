from django.contrib import admin
from .models import Supplier, Product, Currency, Rate, ContactPerson

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Currency)
admin.site.register(Rate)
admin.site.register(ContactPerson)


