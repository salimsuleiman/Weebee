from django.contrib import admin
from .models import Account, AccountType, User, Customer


admin.site.register([User])
admin.site.site_header = 'Weebee administration'
admin.site.site_title = 'Weebee administration panel'

@admin.register(AccountType)
class PersonAdmin(admin.ModelAdmin):
   list_display = ("name", 'maximunWidrawal',)


@admin.register(Account)
class PersonAdmin(admin.ModelAdmin):
   list_display = ("owner","balance", 'accountNumber', 'weebeeAddress', 'lastUpdate', 'accountType', 'accountActivated', 'allowSMS',)
   list_filter = ('accountActivated', )
   # exclude = ['accountNumber']


@admin.register(Customer)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id',"firstName", "lastName", "country",'gender', 'age',)
    list_filter = ('dateOfBirth', 'gender')
    search_fields = ("firstName__startswith", 'lastName__startswith')
    