from django.urls import path, re_path
from .views import register, redirect_view
from django.urls import reverse

urlpatterns = [  
    path('register/', register, name='register'), 
]  