from django.db import models
from django.template import loader
# from accounts.models import Account
from accounts.mail import send_email



class EmailError(models.Model):
    reciever = models.ForeignKey('accounts.Account', verbose_name="reciever", on_delete=models.CASCADE)
    subject = models.CharField(max_length=100,)
    html_path = models.CharField(max_length=200)
    errorType = models.TextField()
    domain = models.CharField(max_length=65, null=False)
    protocol = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.errorType[:]}'

    def requery(self) -> None:
        send_email(html_message=self.html_message, reciever=self.reciever.owner.email, subject=self.subject)
        print('sended')


    @property
    def html_message(self):
        html_message = loader.render_to_string(self.html_path,{
                'domain': self.domain,
                'protocol': self.protocol,
                'account': self.reciever,
                'date': self.date
        })
        return html_message
