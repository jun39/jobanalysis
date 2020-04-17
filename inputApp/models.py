from django.db import models

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
    #  後でテンプレートの整形をする