from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import Employeeserializer


# Create your views here.


def EmployeeApi(APIView):
    employee1 = Employee.objects.all()
    serilizer = Employeeserializer(employee1, many=True)
    return Response(serilizer.data)
