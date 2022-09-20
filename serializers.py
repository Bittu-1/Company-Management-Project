from dataclasses import field
from xml.parsers.expat import model
from rest_framework import serializers
from rest_framework import Employee


class Employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
