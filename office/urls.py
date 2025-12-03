from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('employees/', views.getEmployees),
    path('employees/create/', views.createEmployee),
]
