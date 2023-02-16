from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def about(request):
  return render(request,'about.html')


def club(request):
  data={
    'clublar':Club.objects.all()
  }
  return render(request,'clubs.html',data)

def country(request,son):
  data={
    "oyinchilar":Player.objects.filter(club=son).order_by('tr_narx'),
    'club':Club.objects.get(id=son)
  }
  return render(request,'country-clubs.html',data)

def latest_transfers(request):
  data={
    'transfer':Transfer.objects.all()
  }
  return render(request,'latest-transfers.html',data)

def season(request):
  data={
    'season':Transfer.objects.all()
  }
  return render(request,'2017-18season.html',data)

def u_20_player(request):
  from datetime import date,timedelta
  bugun=date.today()
  boshi=bugun - timedelta(days=(365*20)+5)
  data={
    'oynchi':Player.objects.filter(tug_yil__range=[boshi,bugun]).order_by('-tr_narx','tug_yil'),
    'bugun':bugun.year
  }
  return render(request,'U-20 players.html',data)

def hamma_mavsum(request):
  h_mavsum=HozirgiMavsum.objects.last().mavsum
  data={
    'transferlar':Transfer.objects.filter(mavsum__lt=h_mavsum).values('mavsum').distinct().order_by('mavsum')
  }
  return render(request,'transfer-archive.html',data)

def mavsum(request,mavsum):
  data={
    'transferlar':Transfer.objects.filter(mavsum__startswith=mavsum)
  }
  return render(request,'2017-18season.html',data)


def index(request):
  
  return render(request,'index.html')

def player(request):
      data={
        'oyinchilar':Player.objects.all()
      }
      return render(request,'players.html',data)

def davlat(request,davlat):
  data={
    'davlat':Club.objects.filter(davlat=davlat)
  }
  return render(request,'england.html',data)

def tryouts(request):
  return render(request,'tryouts.html')

def stats(request):
  return render(request,'stats.html')

def courses(request):
  return render(request,'courses.html')
