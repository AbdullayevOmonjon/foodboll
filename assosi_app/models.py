from django.db import models

# Create your models here.
class Club(models.Model):
  nom=models.CharField(max_length=30)
  davlat=models.CharField(max_length=35)
  logo=models.FileField()
  president=models.CharField(max_length=35)
  murabbiy=models.CharField(max_length=30)
  yil=models.DateField()
  eng_katta_herid=models.FloatField()
  eng_katta_sotuv=models.FloatField()
  def __str__(self) -> str:
    return self.nom

class Player(models.Model):
  ism=models.CharField(max_length=30)
  pozitsiya=models.CharField(max_length=35)
  millat=models.CharField(max_length=25)
  tr_narx=models.FloatField()
  tug_yil=models.DateField()
  club=models.ForeignKey(Club,on_delete=models.CASCADE)
  def __str__(self) -> str:
    return self.ism
  
class Transfer(models.Model):
  player=models.ForeignKey(Player,on_delete=models.CASCADE)
  eski=models.ForeignKey(Club,on_delete=models.CASCADE,related_name='sotganlari')
  yangi=models.ForeignKey(Club,on_delete=models.CASCADE)
  narx=models.FloatField()
  tax_narxi=models.FloatField()
  mavsum=models.CharField(max_length=30)
  def __str__(self) -> str:
    return self.player
  
class HozirgiMavsum(models.Model):
  mavsum=models.CharField(max_length=25)
  def __str__(self) -> str:
    return self.mavsum