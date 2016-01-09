from django.db import models
from django.utils import timezone
from college.models import College

# Create your models here.
CATEGORIES = (
    ("Academics", "Academics"),
    ("Sports", "Sports"),
)

class Reviews(models.Model):
    collegeId = models.ForeignKey(College)
    dateAdded = models.DateField(default=timezone.now())
    authorName = models.CharField(max_length=25)
    authorEmail = models.EmailField(max_length=100)
    authorYear = models.IntegerField()
    authorCourse = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    marks = models.FloatField(default="1.00")
    review = models.TextField()

    def __str__(self):
        return self.authorName
        
