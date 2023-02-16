from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
  path('',index,name='index'),
  path('about/',about,name="about"),
  path('latest_transfers/',latest_transfers,name="latest_transfers"),
  path('clubs/',club,name="clubs"),
  path('davlat/<str:davlat>',davlat,name="davlat"),
  path('country/<int:son>/',country,name="country"),
  path('players/',player,name="players"),
  path('tryouts/',tryouts,name="tryouts"),
  path('stats/',stats,name="stats"),
  path('courses/',courses,name="courses"),
  path('mavsum/<str:mavsum>',mavsum,name="mavsum"),
  path('u_20_players/',u_20_player,name="u_20_players"),
  path('transfer_archive/',hamma_mavsum,name="transfer_archive"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)