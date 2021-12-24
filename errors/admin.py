from django.contrib import admin
from .models import *
import pprint
from django.utils.html import format_html
from django.http import HttpResponse


# Register your models here.



@admin.register(EmailError)
class PersonAdmin(admin.ModelAdmin):
   list_display = ("subject", 'html_path', 'protocol', 'date', 'errorType')
#    list_filter = ('accountActivated', )
#    exclude = ['balance', 'accountNumber']
   def make_published(modeladmin, request, queryset):
      for query in queryset:
         try:

            print('=> ALL UNSUCCESSFULL EMAIL MESSAGES ARE BEEN REFRESHED THIS COULD TAKE SOME MINUTES <=')
            query.requery()
            query.delete()
         except BaseException as error:
            pass
         else:
            response = HttpResponse(f'<h1 style="color: green">[{queryset.count()}] emails were successfully refreshed<h1/>')
            return response

      

   actions = [make_published]
   make_published.short_description = "Resend selected email errors"
