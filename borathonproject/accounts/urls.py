from django.urls import path

from accounts.views import *

urlpatterns = [
    path('', index, name='index'),
    path('open_account', open_account, name="open_account")
]