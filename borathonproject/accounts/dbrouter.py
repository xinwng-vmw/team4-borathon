from .models import Account

class AccountsDBRouter:
   def db_for_read (self, model, **hints):
      if (model == Account):
         # your model name as in settings.py/DATABASES
         return 'accounts'
      return None
   
   def db_for_write (self, model, **hints):
      if (model == Account):
         # your model name as in settings.py/DATABASES
         return 'accounts'
      return None