from django.shortcuts import render
from django.views.generic import CreateView

from .models import Trainer
from .forms import TrainerRegistrationForm


def trainer_create_view(request):
    form = TrainerRegistrationForm()
    
    if request.method == "POST":
        form = TrainerRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Trainer.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
            
    context = {"form":form}
    
    return render(request,"trainer/trainer_create.html",context)

class AddTrainerView(CreateView):
    
    model=Trainer
    template_name="trainer/trainer_create.html"
    form_class=TrainerRegistrationForm
   
    def form_valid(self,form):
        print(form.cleaned_data)
        
def ShowTrainerView(request):
    return render(request,'trainer/trainer-table.html')
    
