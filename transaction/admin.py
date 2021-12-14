from django.contrib import admin
from .models import *
from django.contrib import admin


@admin.register(Transfer)
class PersonAdmin(admin.ModelAdmin):
    ...
    # list_display = ("amount", 'date', 'status', 'transtype',)

@admin.register(Transaction)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("amount", 'date', 'status', 'transtype',)
    list_filter = ('status',)

    exclude = ['previous_balance', 'current_balance', 'balanceAfterTransaction']
