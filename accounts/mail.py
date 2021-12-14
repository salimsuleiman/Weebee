from django.core.mail import BadHeaderError, send_mail
from django.conf import settings

def send_email(html_message, reciever, subject):   
        send_mail(
            from_email=settings.FROM_EMAIL,
            subject=subject,
            recipient_list=[reciever],
            html_message=html_message,
            fail_silently=False,
            message=None,
        )