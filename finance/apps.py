from django.apps import AppConfig

class FinanceConfig(AppConfig):
    name = 'finance'
    verbose_name = 'Finance'
    def ready(self):
        return super().ready()
    
    