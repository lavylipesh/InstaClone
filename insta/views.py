from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import InstaForm
from django.contrib.auth.decorators import login_required
from .models import Image

@login_required(login_url='/accounts/login/')
def index(request):
    images = Image.objects.all()
    return render(request,'index.html',{'images':images})

def search_results(request):
    if  'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_name(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"profiles":searched_profiles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
