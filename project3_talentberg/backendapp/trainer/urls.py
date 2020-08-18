from django.urls import path
from .views import AddTrainerView,ShowTrainerView,UpdateTrainerView,DeleteTrainerView


urlpatterns = [
    path("create/",AddTrainerView.as_view(),name="trainer-create"),
    path("show/",ShowTrainerView.as_view(),name="trainer-show"),
    path("<int:id>/update/",UpdateTrainerView.as_view(),name="trainer-update"),
    path("<int:pk>/delete/",DeleteTrainerView.as_view(),name="trainer-delete"),
]