from django.shortcuts import render
from .forms import RawTrainerForm

# Create your views here.

def trainer_create_view(request):
    form = RawTrainerForm()
    
    if request.method == "POST":
        form = RawTrainerForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Trainer.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
            
    context = {"form":form}
    
    return render(request,"trainer/trainer_create.html",context)
