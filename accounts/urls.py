from django.urls import path
from .views import *



urlpatterns = [
    path('create-customer/', CreateCustomer),
    path('create-account/<int:customerID>/', CreateAccount),
]