from django.db import models
from django.utils import timezone

# Create your models here.

class College(models.Model):
    datePublished = models.DateField(default=timezone.now())
    name = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    location = models.CharField(max_length=50)
    pin = models.BigIntegerField()
    phone = models.BigIntegerField()
    email = models.EmailField()
    website = models.CharField(max_length=100)
    coed = models.CharField(max_length=3)
    seats = models.IntegerField()
    acceptanceRate = models.FloatField()

    def __str__(self):
        return self.name

class Common(models.Model):
    collegeId = models.ForeignKey(College)

    class Meta:
        abstract = True

class Academics(Common):
    courses = models.TextField()
    avgFees = models.FloatField()
    graduationRate = models.IntegerField()

class Sports(Common):
    facilities = models.TextField()
    popular = models.TextField()

class AvgMarks(models.Model):
    collegeId = models.ForeignKey(College)
    overall = models.FloatField()
    academics = models.FloatField()
    sports = models.FloatField()
