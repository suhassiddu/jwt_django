from django.http import Http404, HttpRequest
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class Protected(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({
            'msg': 'This message is from protected URL, and only with proper credentials can access it'
        })

class Public(APIView):
    def get(self, request):
        return Response({
            'msg': 'This message is from public URL, and any body can access this without credentials'
        })
