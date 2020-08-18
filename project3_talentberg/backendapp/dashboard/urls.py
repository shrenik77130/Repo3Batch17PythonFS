from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="dashboard-index"),
    path("dashboard/course/all/",views.getCourseChartData,name="dashboard-coursegraph")
]
