from django.shortcuts import render
from .forms import StudentForm

def student_create_view(request):
    form = StudentForm()
    
    if(request.method=="POST"):
        form.save()

    context ={ "form":form }
    
    return render(request,"student/student_create.html",context)