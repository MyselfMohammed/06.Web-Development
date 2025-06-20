
from django.db import models

# Create your models here.
class Concrete_Model(models.Model): 
    Cement = models.FloatField()
    Slag = models.FloatField()
    Flyash = models.FloatField()
    Super_Plasticizer = models.FloatField()
    Coarse_Aggregate = models.FloatField()
    Fine_Aggregate = models.FloatField()
    Water = models.FloatField()
    Curing_Age_in_Days = models.IntegerField()
    