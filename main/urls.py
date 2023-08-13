from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    #path('about', views.about, name='about'),
    #path('contacts', views.contacts, name='contacts'),
    path('downloadyoutubevideo', views.DownloadYoutubeVideo, name='downloadyoutubevideo'),
    path('downloadinstagrammedia', views.downloadmediainstagram, name='downloadinstagrammedia'),
    path('convertfiles', views.convertfiles, name='convertfiles')
]