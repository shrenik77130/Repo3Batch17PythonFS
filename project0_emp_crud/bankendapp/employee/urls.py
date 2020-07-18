from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="employee-index"),
    path('getall/',views.getAllEmployees,name="employee-getAll"),
    path('empsave/',views.insertEmpRecord,name="employee-save")
]
