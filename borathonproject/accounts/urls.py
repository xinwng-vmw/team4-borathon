from django.urls import path

from accounts.views import *

urlpatterns = [
    path('', index, name='index'),
    path('open_account', open_account, name="open_account"),
     # account/?account_number=ACTNUMHERE
    path('get_customer_account', get_customer_account, name="account_number")
    
]