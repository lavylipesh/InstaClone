from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^search/',views.search_results,name='search_results'),
    url(r'^profile/$',views.profile,name='profile') ,
    url(r'^like/(\d+)',views.like, name="like"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
