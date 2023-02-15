from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
  list_display=('id','nom','davlat','logo','president','murabbiy','yil','eng_katta_herid','eng_katta_sotuv')
  list_editable=('president','murabbiy','eng_katta_herid','eng_katta_sotuv')
  list_display_links=('nom','davlat')
  search_fields=('nom','davlat')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
  list_display=('id','ism','pozitsiya','millat','tr_narx','tug_yil','club')
  list_editable=('tr_narx','club')
  list_display_links=('id','ism')
  search_fields=('ism','tr_narx','club')
  
  
@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
  list_display=('id','player','eski','yangi','narx','tax_narxi','mavsum')
  list_editable=('eski','yangi','narx','tax_narxi','mavsum')
  autocomplete_fields=('player','eski','yangi')
  list_display_links=('player',)
  search_fields=('player','narx','mavsum')
  
@admin.register(HozirgiMavsum)
class HozirgiMavsum(admin.ModelAdmin):
  list_display=('mavsum',)
  
