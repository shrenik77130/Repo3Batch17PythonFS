from django.urls import path
from . import views


urlpatterns = [
    path("create/",views.trainer_create_view,name="trainer.createTrainer")
]