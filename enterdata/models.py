from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT

class Country(models.Model):
    in_country = models.CharField(max_length=50)

    class Meta: 
        ordering = ['in_country']

    def __str__(self):
        return self.in_country
    
class County(models.Model):
    name = models.CharField(max_length=50)
    in_country = models.ForeignKey(Country, default = 1, max_length=50, on_delete=PROTECT)
    #postcode = models.CharField(max_length=50, blank = True)

    class Meta: 
        ordering = ['name']

    def __str__(self):
        return self.name

class Species(models.Model):
    name = models.CharField(max_length=30)
    date_seen = models.DateField()
    photo = models.ImageField(default ='default.png', blank = True)
    in_country = models.ForeignKey(Country, default = 1, max_length=50, on_delete=PROTECT)
    county = models.ForeignKey(County, default = 1, max_length=50, on_delete=PROTECT)
    #sound_file = models.FileField(upload_to=/'sounds/')
    #class Meta:
    # db_table='Audio_store'
    # maybe later add user 
    birder = models.ForeignKey(User, on_delete = PROTECT, default=None)

    def __str__(self): 
        return self.name  #function to return the name of the instance of Species