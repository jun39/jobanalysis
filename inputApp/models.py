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
            return ' id名:' + str(self.id) + ',' + self.company

class Comment(models.Model):
        company = models.ForeignKey(Company, on_delete=models.CASCADE)
        title = models.CharField(max_length=100)
        content = models.CharField(max_length=300)
        pub_date = models.DateTimeField(auto_now_add=True)
        def __str__(self):
            return '<company:id=' + str(self.id) + ',' + str(self.company) + '(' + str(self.pub_date) +')>'
        class Meta:
            ordering = ('pub_date',)

class Industry(models.Model):
        industry_name = models.CharField(max_length=50)
        def __str__(self):
            return 'industry:id'+str(self.id) + '業界名'+ str(self.industry_name)