from django.urls import path
from CMSApp.views import EmployeeApi


urlpatterns = [
    path('Employeeapi', EmployeeApi),
]
