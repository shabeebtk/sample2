from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.


class Tenants(TenantMixin):
    name = models.CharField(max_length=150)
    created_on = models.DateField(auto_now_add=True)
    
    auto_create_schema = True
    
class Domain(DomainMixin):
    pass