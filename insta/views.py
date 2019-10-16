from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Image
from django.views.generic import RedirectView

@login_required(login_url='/accounts/register/')
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

def profile(request):
    current_user=request.user
    image=Image.objects.filter(profile_id=current_user.id)
    return render(request,'profile.html',{'image':image})

@login_required(login_url='/accounts/login/')
def like(request,image_id):

  image = Image.objects.get(pk = image_id)

  is_liked = False
  if image.likes.filter(id = request.user.id).exists():
      image.likes.remove(request.user)
      is_liked = False
  else:
      image.likes.add(request.user)
      is_liked = True

  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def total_likes(self):
      self.likes.count()

def comment(request):
    if request.method == 'POST':
        Form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['your_comment']
            comment.save()
            HttpResponseRedirect('index')
    else:
        form = CommentForm()
    return render(request,'index.html',{"letterform":form})
