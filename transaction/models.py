from django.db import models
from accounts.models import *
from django.contrib import messages
from django.core.exceptions import ValidationError


TRANSACTION_STATUS = [
  (0, 'Initiated'),
  (1, 'Declined'),
  (2, 'Aborted'),
  (3, 'Successful')
]

TRANSACTION_TYPE = [
    (0, 'Debit'),
    (1, 'Credit')
]


class DebitRelation(models.Model):
    credit = models.OneToOneField('Transaction', on_delete=models.CASCADE, null=True, related_name='a1')
    debit = models.OneToOneField('Transaction', on_delete=models.CASCADE, null=True, related_name='b2')


class Transaction(models.Model):
    amount =  models.DecimalField(
        default=0.0,
        max_digits=12,
        decimal_places=2
    )
    naration = models.TextField(help_text="Naration of transfer")
    date = models.DateTimeField(auto_now=True, null=True)
    beneficiary = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='reciever')
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='sender')
    transtype = models.IntegerField(choices=TRANSACTION_TYPE, verbose_name='Transaction Type', null=True)
    status = models.IntegerField(choices=TRANSACTION_STATUS)
    previous_balance=models.DecimalField(default=0,max_digits=20,decimal_places=2)
    current_balance=models.DecimalField(default=0,max_digits=20,decimal_places=2)

    def __str__(self):
        return f'F/[ {self.sender.getFullName[:15]} ]      TO/[ {self.beneficiary.getFullName[:15]} ]'


class Transfer(models.Model):
    amount =  models.DecimalField(
        default=0.0,
        max_digits=12,
        decimal_places=1
    )
    naration = models.TextField(help_text="Naration of transfer", blank=True, null=True, default="")
    AccountNumber = models.CharField(max_length=150, blank=True)
    WeebeeAddress = models.CharField(max_length=150, blank=True)
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='credits')

    def __str__(self):
        return f'{self.amount}'

    def clean(self):
        beneficiary = Account.objects.filter(accountNumber=self.AccountNumber).first()
        if beneficiary is None:
            if Account.objects.filter(weebeeAddress=self.WeebeeAddress).first() is None:
                raise ValidationError(('Unknown Beneficiary'))
        beneficiary = Account.objects.filter(weebeeAddress=self.WeebeeAddress).first()

        if self.sender.weebeeAddress == self.WeebeeAddress:
            raise ValidationError(('You cannot transfer money to your weebee address'))
        elif self.sender.accountNumber == self.AccountNumber:
            raise ValidationError(('You cannot transfer money to your account Number'))
        
        if self.sender.balance < self.amount:
            raise ValidationError(('Insuffiecient Balance'))
        else:
            # create transaction
            transaction = Transaction(
                naration=self.naration,
                amount=self.amount,
                beneficiary=beneficiary,
                status=3,
                transtype=0,
                previous_balance=self.sender.balance,
                sender=self.sender
            )

            # debit
            self.sender.balance = self.sender.balance - self.amount
            self.sender.save()
            transaction.current_balance= self.sender.balance
            transaction.save()

            # deposit | 0
            # credit  | 1
            Beneficiarytransaction = Transaction(
                naration=self.naration,
                amount=self.amount,
                beneficiary=beneficiary,
                status=3,
                transtype=1,
                previous_balance=beneficiary.balance,
                sender=self.sender
            )
            Beneficiarytransaction.save()

            # credit
            beneficiary.balance = beneficiary.balance + self.amount
            beneficiary.save()
            Beneficiarytransaction.current_balance = beneficiary.balance
            Beneficiarytransaction.save()

            DebitRelation(credit=Beneficiarytransaction, debit=transaction).save()


from django.dispatch import receiver
@receiver(post_save, sender=DebitRelation)
def send_transaction_email(sender, instance=None, created=False, **kwargs):
    if created:
        context = {
                    'domain': 'localhost:8000',
                    'protocol': 'https',
                    'account': instance.credit.sender,
                    'transaction': instance.debit,
                    'Transtype': 'debit',
        }

        DebitMessage = loader.render_to_string('mail/alert.html', context)
        subject = '[Weebee] Your account was debited'
        try:
            send_email(html_message=DebitMessage, reciever=instance.debit.sender.owner.email, subject=subject)
        except BaseException as error:
            EmailError(
                reciever=instance.debit.sender,
                subject='', domain='localhost:8000',
                protocol='https',
                html_path='mail/alert.html',
                errorType=error
            ).save()



        context = {
                    'domain': 'localhost:8000',
                    'protocol': 'https',
                    'account': instance.credit.beneficiary,
                    'transaction': instance.credit,
                    'Transtype': 'credit',
        }
        CreditMessage = loader.render_to_string('mail/alert.html', context)

        subject='[Weebee] Your account was debited'
        try:
            send_email(html_message=CreditMessage, reciever=instance.credit.beneficiary.owner.email, subject=subject)
        except BaseException as error:
            EmailError(
                reciever=instance.credit.sender,
                subject='', domain='localhost:8000',
                protocol='https',
                html_path='mail/alert.html',
                errorType=error
        ).save()
           