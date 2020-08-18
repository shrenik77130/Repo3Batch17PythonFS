from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.urls import reverse

from .models import Trainer
from .forms import TrainerRegistrationForm


class AddTrainerView(CreateView):
    
    model=Trainer
    template_name="trainer/trainer_create.html"   #trainer_create.html
    form_class=TrainerRegistrationForm
   
    success_url="/trainer/create"
    
        
class ShowTrainerView(ListView):
    model=Trainer
    template_name="trainer/trainer-table.html"      #trainer_list.html
    
    # def get_queryset(self, *args, **kwargs): 
    #     qs = super(GeeksList, self).get_queryset(*args, **kwargs) 
    #     qs = qs.order_by("-id") 
    #     return qs     
    
class UpdateTrainerView(UpdateView):

    model=Trainer
    template_name="trainer/trainer_create.html"
    form_class=TrainerRegistrationForm
   
    success_url="/trainer/create"
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Trainer,id=id_)
    
class DeleteTrainerView(DeleteView):
    model=Trainer
    template_name="trainer/trainer_delete.html"
    success_url="/trainer/show"
    
    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(Trainer,id=id_)    
    
    
    # def get_success_url(self):
    #     return reverse("trainer:trainer-show")
    
    
    
    
    
    
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
