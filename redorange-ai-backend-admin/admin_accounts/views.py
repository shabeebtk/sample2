from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
import requests
from .utils import create_tokens_for_user, blacklist_token

# Create your views here.

class Test(APIView):
    def get(self, request):
        response = requests.get('http://localhost:9000/test')
        data = response.json()
        return Response(data)
    
    
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            return Response('Invalid credentials')

        access_token, refresh_token = create_tokens_for_user(user)
        return Response({'access_token': access_token, 'refresh_token' : refresh_token})
    
    
class GetUser(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        
        print(user)
        return Response({'user' : user.email})
    
    
class UserLogout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        access_token = request.headers.get('Authorization').split(' ')[1]
        refresh_token = request.data.get('refresh_token')

        if access_token:
            blacklist_token(access_token)

        if refresh_token:
            blacklist_token(refresh_token)

        return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
    
