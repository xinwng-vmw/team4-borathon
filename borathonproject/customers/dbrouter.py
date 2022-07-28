class CustomersDBRouter:
   def db_for_read (self, model, **hints):
      if (model == Customer):
         # your model name as in settings.py/DATABASES
         return 'customers'
      return None
   
   def db_for_write (self, model, **hints):
      if (model == Customer):
         # your model name as in settings.py/DATABASES
         return 'customers'
      return None