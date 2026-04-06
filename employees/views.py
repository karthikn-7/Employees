from django.shortcuts import get_object_or_404
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import EmployeeSerializer
from rest_framework import status

class EmployeeView(APIView):
    
    def get(self,request, id=None):
        
        if not id:
            
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        try:
            employee = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({"Employee not found!"},status=status.HTTP_400_BAD_REQUEST)
        
        
    def post(self, request):
        print(request.data)
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        
        try:
            employee = Employee.objects.get(id=id)
            employee.delete()
            return Response([],status = status.HTTP_204_NO_CONTENT)
        
        except Employee.DoesNotExist:
            return Response({"Employee not found!"},status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):
        
        try:
            employee = Employee.objects.get(id)
            serializer = EmployeeSerializer(data = request.data)
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        except Employee.DoesNotExist:
            return Response({"Employee not found!"},status=status.HTTP_400_BAD_REQUEST)


