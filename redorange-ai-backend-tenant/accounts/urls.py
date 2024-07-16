from django.urls import path
from .views import TenantTest

urlpatterns = [
    path('test-tenant', TenantTest.as_view(), name='tenant test')
]
