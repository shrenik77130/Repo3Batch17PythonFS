from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.views.generic.list import ListView

from .models import CourseMaster
from .forms import CourseRegistrationForm


class AddCourseView(CreateView):
    
    model=CourseMaster
    template_name="course/course_create.html"
    form_class=CourseRegistrationForm
   
    success_url="/course/create"
    
        
class ShowCourseView(ListView):
    model=CourseMaster
    template_name="course/course-table.html"
    
    # def get_queryset(self, *args, **kwargs): 
    #     qs = super(GeeksList, self).get_queryset(*args, **kwargs) 
    #     qs = qs.order_by("-id") 
    #     return qs     
    
class UpdateCourseView(UpdateView):

    model=CourseMaster
    template_name="course/course_create.html"
    form_class=CourseRegistrationForm
   
    success_url="/trainer/create"
