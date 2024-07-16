from django.urls import path
from .views import Test
from django.contrib import admin


urlpatterns = [
    path('test', Test.as_view(), name='test')
]
