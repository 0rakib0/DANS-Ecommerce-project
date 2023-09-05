from django.db import models
from Accounts.models import User
from orderApp.models import Order
# Create your models here.\

class Billing_Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='billing_address')
    address = models.CharField(max_length=20, null=True, blank=True)
    zipeCode = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return str(self.user.profile.full_name)+ "'s Billling Address"
    

    def is_fully_filed(self):
        # all field name stor in fields_name
        fields_name=[f.name for f in self._meta.get_fields()] 
        for field_name in fields_name:
            value = getattr(self, field_name)
            if value is None or value=='':
                return False
        return True