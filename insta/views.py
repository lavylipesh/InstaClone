from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def search_results(request):
    if  'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_names = bio.search_by_name(search_term)
        message = f"{search_term}"

        return render(request,'search.html',{"message":message,"names":searched_names})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
