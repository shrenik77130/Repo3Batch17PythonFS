from django.urls import path
from .views import AddCourseView,ShowCourseView,UpdateCourseView


urlpatterns = [
    path("create/",AddCourseView.as_view(),name="course-create"),
    path("show/",ShowCourseView.as_view(),name="course-show"),
    # path("<pk>/update/",UpdateTrainerView.as_view(),name="trainer-update"),
]