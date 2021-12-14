from django.db import models
from accounts.models import *


# class TransactionType(models.Model):
#     name = models.CharField(max_length=20)
#     description = models.TextField()
#     def __str__(self):
#         return self.name

TRANSACTION_STATUS = [
  (0, 'Initiated'),
  (1, 'Declined'),
  (2, 'Aborted'),
  (3, 'Successful')
]

TRANSACTION_TYPE = [
    (0, 'Deposit'),
    (1, 'Credit'),
]

class Transfer(models.Model):
    amount =  models.DecimalField(
        default=0.0,
        max_digits=12,
        decimal_places=2
    )
    naration = models.TextField(help_text="Naration of transfer")
    AccountNumber = models.CharField(max_length=150, blank=True)
    WeebeeAddress = models.CharField(max_length=150, blank=True)
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='credits')



class Transaction(models.Model):
    date = models.DateTimeField(auto_now=True, null=True)
    amount =  models.DecimalField(
        default=0.0,
        max_digits=12,
        decimal_places=2
    )
    reciever = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='reciever')
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='sender')
    transtype = models.IntegerField(choices=TRANSACTION_TYPE, verbose_name='Transaction Type', null=True)
    status = models.IntegerField(choices=TRANSACTION_STATUS)

    previous_balance=models.DecimalField(  default=0,max_digits=20,decimal_places=2)
    current_balance=models.DecimalField(  default=0,max_digits=20,decimal_places=2)
    # RefNumber = models.CharField(max_length=60, default=getRefNumber(Transaction))

    def getRefNumber(self):
        # rn = f'WEEB//{self.date.day}/{self.date.second+7}/{if self.transtype == 0 }/{self.id}'.upper()
        # # self.RefNumber = rn
        # return rn
        return ''
    





    def __str__(self):
        return self.getRefNumber()

    balanceAfterTransaction = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=12
    )