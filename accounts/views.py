from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':

        form = UserCreationForm()
        return render(request,'signup.html',{'form':form})
