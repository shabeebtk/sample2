from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class TenantTest(APIView):
    def get(self, request):
        return Response({'message' : 'tenant only'})