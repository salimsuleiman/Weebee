from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from .constants import *
from django.dispatch import receiver
from .mail import send_email
from django.db.models.signals import post_save
from django.template import loader
from django.contrib.sites.shortcuts import get_current_site
from django_countries.fields import CountryField
from datetime import datetime
from errors.models import EmailError

# uuidField = uuid.UUID()


class User(AbstractUser):
  ...




class Customer(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(verbose_name='First Name',max_length=60, null=False)
    lastName = models.CharField(verbose_name='Last Name',max_length=60, null=False)
    middleName = models.CharField(verbose_name='Middle Name', default="", max_length=50, blank=True, null=True)
    dateOfBirth = models.DateField(verbose_name="Date of birth",auto_now=False)

    # contact
    phoneNumber = models.CharField(max_length=20, null=False)
    email= models.EmailField(null=False, blank=True,)
    stateOfOrigin = models.CharField(verbose_name='State of origin', max_length=20, choices=STATES,  null=False)
    idCardNumber = models.CharField(verbose_name='Identity card', max_length=20, null=False)

    gender = models.CharField(max_length=20, null=False, choices=GENDER_CHOICES, default=0)
    dateJoined = models.DateTimeField(verbose_name='date joined',auto_now=True)
    # address
    address = models.TextField(null=False)
    state = models.CharField(max_length=20, choices=STATES, default=7, null=False)
    postalCode = models.DecimalField(verbose_name='postal code', decimal_places=0, max_digits=9)
    city = models.CharField(max_length=256)
    country = CountryField()

    @property
    def getFullName(self):
        return f'{self.lastName.upper() } {self.firstName.upper()}'

    @property
    def age(self):
        return int((datetime.now().date() - self.dateOfBirth).days / 365.25)

    def __str__(self):
        return f'{self.getFullName} {self.age}'


class AccountType(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    maximunWidrawal = models.DecimalField(decimal_places=2,max_digits=12)
    def __str__(self):
        return self.name + ' Account'



class Account(models.Model):
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    weebeeAddress = models.CharField(max_length=200, unique=True, default='@weebee.com', verbose_name='Weebee Address', blank=True)
    accountNumber = models.CharField(max_length=15, verbose_name='Account Number', unique=True, blank=True)
    owner = models.ForeignKey(Customer, null=False, unique=True, default=None, on_delete=models.CASCADE, related_name='accounts')
    date_created = models.DateTimeField(auto_now=True)
    accountType = models.ForeignKey(AccountType, verbose_name='Account type', default=None, null=False, on_delete=models.CASCADE)
    accountActivated = models.BooleanField(default=True, verbose_name='Account activated',  blank=False)
    allowSMS = models.BooleanField(default=True, verbose_name='allowed sms?', blank=False)
    initialDepositDate = models.DateTimeField(verbose_name='Initial deposit', null=True, blank=True)
    lastUpdate = models.DateTimeField(auto_now=True, verbose_name='last updated', null=True)

   

    def deactived(self):
        self.accountActivated = True
        self.save()

    @property
    def getFullName(self):
        return f'{self.owner.lastName } {self.owner.firstName} {self.owner.middleName}'.upper()

    def __str__(self):
        return self.getFullName



@receiver(post_save, sender=Account)
def send_email_to_new_user(sender, instance=None, created=False, **kwargs):
    html_message = loader.render_to_string('mail/account_create.html',{
                'domain': 'localhost:8000',
                'protocol': 'https',
                'account': instance,
    })

    if created:
        try:
            send_email(html_message=html_message, reciever=instance.owner.email, subject='[Weebee] Your account is create')
        except BaseException as error:
            EmailError(reciever=instance, subject='New Account Set up', domain='localhost:8000' ,protocol='https',html_path='mail/account_create.html',  errorType=error).save()