from django.http import HttpResponse  
from django.shortcuts import render  
from django.contrib.auth import login, authenticate  
from .forms import CustomUserCreationForm  
from django.contrib.auth.models import User  
from django.contrib.auth import get_user_model


  
def register(request):  
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():  
            user = form.save()  
            user.is_active = True
            user.role = "Participant"  
            user.save()
    else:  
        form = CustomUserCreationForm()  
    return render(request, 'sign_up.html', {'form': form})  


