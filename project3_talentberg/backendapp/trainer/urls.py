from django.urls import path
from .views import AddTrainerView,ShowTrainerView


urlpatterns = [
    path("create/",AddTrainerView.as_view(),name="trainer-create"),
    path("show/",ShowTrainerView,name="trainer-show"),
]