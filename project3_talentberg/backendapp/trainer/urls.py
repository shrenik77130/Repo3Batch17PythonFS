from django.urls import path
from .views import AddTrainerView,ShowTrainerView,UpdateTrainerView


urlpatterns = [
    path("create/",AddTrainerView.as_view(),name="trainer-create"),
    path("show/",ShowTrainerView.as_view(),name="trainer-show"),
    # path("<pk>/update/",UpdateTrainerView.as_view(),name="trainer-update"),
]