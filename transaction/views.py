from random import seed
from django.shortcuts import render
from accounts.models import *
from .models import *
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from accounts.mail import send_email

@api_view(['POST'])
def transferWeeb(request):
    data = request.data
    transactionType = TransactionType.objects.filter(name='Credit').first()

    sender = Account.objects.filter(id=1).first()
    receiver = Account.objects.filter(id=2).first()
    

    transaction = Transaction(amount=int(data['amount']), reciever=receiver, sender=sender, transtype=transactionType, balanceAfterTransaction=sender.balance)
    senderBeforeBalace = sender.balance 
    recieverBeforeBalance = receiver.balance 

    receiver.balance = recieverBeforeBalance + int(data['amount'])
    sender.balance = senderBeforeBalace - int(data['amount'])

    receiver.save()
    sender.save()
    transaction.save()

    send_email(reciever=sender.owner.email, subject="Debit Alert", message=f"""
        {sender.owner.getFullName()}
            you account have been debited {int(data['amount'])} Weebs
            Amount: ₩ {int(data['amount'])}
            reciver: {receiver.weebeeAddress}

            Balance Before: ₩ {senderBeforeBalace} 
            Balance After: ₩ {sender.balance} 
    """)


    return Response({})