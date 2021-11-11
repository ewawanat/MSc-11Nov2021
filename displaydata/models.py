from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
from enterdata.models import Country, County

class DisplayForm(models.Model):
    species_name = models.CharField(max_length=30)
    in_country = models.ForeignKey(Country, default = 1, max_length=50, on_delete=PROTECT)
    county = models.ForeignKey(County, default = 1, max_length=50, on_delete=PROTECT)    
    from_date = models.DateField()
    to_date = models.DateField()
#  birder = models.ForeignKey(User, on_delete=CASCADE, default=None)

    def __str__(self): 
        return self.species_name  #function to return the name of the instance of DisplayForm