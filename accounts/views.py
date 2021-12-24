from rest_framework.response import Response
from .models import Customer, Account, AccountType
from rest_framework.decorators import api_view
import django 
from .functions import generate_account_number
from .models import Customer
from .functions import *
from .forms import *
from django.shortcuts import get_object_or_404
import accounts

@api_view(['POST'])
def CreateCustomer(request):
    form = CreateCustomerForm(request.data)
    if form.is_valid():
        if form.instance.age >= 18:
            form.save()
            return Response({'detail': 'customer is successfully created.'})
        else:
            return Response({'error': 'valid age must be above 18 above'})
    else:
        errors = dict(form.errors)
        return Response(errors)


@api_view(['POST'])
def CreateAccount(request, customerID):
    customer = get_object_or_404(Customer, id=customerID)

    try:
        accountType = AccountType.objects.get(name=request.data['accountType'])
        
    except accounts.models.AccountType.DoesNotExist:
        return Response({'accountType': ['ivalid account type defination']})
    except KeyError:
        return Response({'accountType': ['This field is required.']})

    try:
        account = Account(
            owner=customer,
            accountNumber=generate_account_number(),
            weebeeAddress=f"{customer.firstName}{customer.id}@weebee.com",
            accountType=accountType
        )
        account.save()
        return Response({'success': [f'[{customer.getFullName}] account successfully opened account']})
    except django.db.utils.IntegrityError:
        return Response({'error': ['This is customer already has an account']})
   

    