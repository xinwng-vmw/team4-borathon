from .models import Transaction

class TransactionsDBRouter:
   def db_for_read (self, model, **hints):
      if (model == Transaction):
         # your model name as in settings.py/DATABASES
         return 'transactions'
      return None
   
   def db_for_write (self, model, **hints):
      if (model == Transaction):
         # your model name as in settings.py/DATABASES
         return 'transactions'
      return None