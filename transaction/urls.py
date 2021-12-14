from django.urls import path
from .views import *



urlpatterns = [
    path('transfer/', transferWeeb)
    # path('create-account/'),
]