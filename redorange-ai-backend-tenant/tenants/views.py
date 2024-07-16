from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class Test(APIView):
    def get(self, request):
        print(request.get_host())
        data = { 
            'tenant_id' : '1',
            'tenant_name' : 'caretcloud'
        }
        return Response(data)