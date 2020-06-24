from django.db import models

# Create your models here.
class Member(models.Model):
    id=models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    city=models.CharField(max_length=20)

    def __str__(self):
        return self.id
class Activity(models.Model):
    id1=models.ForeignKey(Member,on_delete=models.CASCADE)
    startDate=models.CharField(max_length=10)
    endDate=models.CharField(max_length=10)
    startTime=models.CharField(max_length=15)
    endTime=models.CharField(max_length=15)


