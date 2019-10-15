from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import InstaForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Image

@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.objects.all()
    return render(request,'index.html',{'images':images})

def search_results(request):
    if  'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = Profile.search_by_user(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"users":searched_users})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
