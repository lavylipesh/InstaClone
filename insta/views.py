from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import InstaForm

def index(request):
    if request.method == 'POST':
        form = InstaForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            recipient == InstaRecipiient(name=name,email=email)
            recipient.save()
            HttpResponseRedirect('index')
        else:
            form = InstaForm()

    return render(request,'index.html',{"letterForm":form})

def search_results(request):
    if  'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_name(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"profiles":searched_profiles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
