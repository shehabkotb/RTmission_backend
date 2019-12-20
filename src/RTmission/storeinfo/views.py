from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserInfoForm
from .models import UserInfo

def home_view(request, *arg, **kwargs):
    form = UserInfoForm(request.POST or None)
    if (form.is_valid()):
        form.save()
        
        # clearing the form after submitting
        form = UserInfoForm()

    context = {
        'form' : form
    } 
    
    return render(request, "home.html", context)