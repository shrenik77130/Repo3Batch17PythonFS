from django.urls import path
from .views import AddTrainerView


urlpatterns = [
    path("create/",AddTrainerView.as_view(),name="trainer.createTrainer")
]