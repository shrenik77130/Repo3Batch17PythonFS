from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.views.generic.list import ListView

from .models import Trainer
from .forms import TrainerRegistrationForm


class AddTrainerView(CreateView):
    
    model=Trainer
    template_name="trainer/trainer_create.html"
    form_class=TrainerRegistrationForm
   
    success_url="/trainer/create"
    
        
class ShowTrainerView(ListView):
    model=Trainer
    template_name="trainer/trainer-table.html"
    
    # def get_queryset(self, *args, **kwargs): 
    #     qs = super(GeeksList, self).get_queryset(*args, **kwargs) 
    #     qs = qs.order_by("-id") 
    #     return qs     
    
class UpdateTrainerView(UpdateView):

    model=Trainer
    template_name="trainer/trainer_create.html"
    form_class=TrainerRegistrationForm
   
    success_url="/trainer/create"
    
    
    
    
    
    
    
    
    
'''
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
'''    
