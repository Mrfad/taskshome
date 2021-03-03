from django.forms import ModelForm
from .models import Supplier, ContactPerson


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'supplier_name',
            'supplier_phone',
            'supplier_address',
            'email',
            'website',
            'notes',
        ]


class ContactForm(ModelForm):
    class Meta:
        model = ContactPerson
        fields = ['contact_name',
                'contact_mobile',
                'email',
                'Job_title',
                'description']