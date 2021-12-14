from rest_framework.response import Response
from .models import Customer, Account, AccountType
from rest_framework.decorators import api_view, permission_classes, authentication_classes
import django 
from .functions import generate_account_number, create_customer_instant
from .models import Customer
from .functions import *

@api_view(['POST'])
def createSignup(request):
    """New Customer and Account Set up"""
    print(request.data)


    
    # customerAccountType = AccountType.objects.filter(name=request.data['AccountType']).first()
    # try:
    #     customer = create_customer_instant(request.data, Customer)
    # except django.utils.datastructures.MultiValueDictKeyError:
    #     return Response({'detail': 'data is Not Complete'})     

    # if request.data['AccountType'].title() not in ['Credit', 'Debit']:
    #     return Response({'detail': 'InValid Account Type'})
    # if customerAccountType == None:
    #     return Response({'detail': 'InValid account type'})
    # try:
    #     customer.save()
    #     account = Account(
    #         owner=customer,
    #         accountNumber=f'00{generate_account_number(10)}',
    #         accountType=customerAccountType
    #     )
    #     account.save()
    # except django.core.exceptions.ValidationError:
    #     return Response({'detail': 'Invalid Date format It must be in YYYY-MM-DD format.'})
    # else:
    #     return Response({'detail': 'customer is successfully created.'})