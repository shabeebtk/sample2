from django.urls import path
from .views import LoginView, GetUser

urlpatterns = [
   path('login', LoginView.as_view(), name='user login'),
   path('get/user', GetUser.as_view(), name='user data'),
]
