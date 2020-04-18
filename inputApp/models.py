from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Company(models.Model):
     company = models.CharField(max_length=50)
     location = models.CharField(max_length=50)
     office = models.CharField(max_length=50)
     establishment = models.IntegerField()
     capitalStock = models.IntegerField()
     sales = models.IntegerField()
     employees = models.IntegerField()
     averageAge = models.IntegerField()
     startingSales = models.IntegerField()
     workingHours = models.IntegerField()
     def __str__(self):
        return '<company:id=' + str(self.id) + ',' + \
            self.company + '(' + str(self.sales) +')>'