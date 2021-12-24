from django.forms import ModelForm
from .models import *



class CreateCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstName', 'lastName', 'dateOfBirth', 'country',
                  'phoneNumber', 'email', 'stateOfOrigin', 'idCardNumber',
                  'state', 'gender', 'address', 'postalCode', 'city', 'state',
                  'idCardNumber', 'middleName', 'email',]