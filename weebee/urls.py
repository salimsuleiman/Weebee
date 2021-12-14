from django.contrib import admin
from django.urls import path


from django.shortcuts import render
from django.urls.conf import include


def index(request):
    return render(request, 'index.html')


urlpatterns = [
    path('', index),
    path('transactions/', include('transaction.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
