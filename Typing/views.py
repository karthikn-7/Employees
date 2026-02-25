from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TypingResponse
from .serializer import TypingSerializer

# microservices for typing app


class TypingViewSet(APIView):

    def get(self, request):
        data = TypingResponse.objects.all()
        serializer = TypingSerializer(data, many=True)
        print(serializer)
        return Response(serializer.data)
    
    def post(self, request):
        print(dir(request))
        print(request.data)
        serializer = TypingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)