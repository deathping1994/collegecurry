from django.core.management.base import BaseCommand, CommandError
from django.db.models import Avg
from college.models import AvgMarks, College
from reviews.models import Reviews

class Command(BaseCommand):
    help = "Calculates and save the average for a particular field"

    def handle(self, *args, **options):
        colleges = College.objects.all()
        for i in colleges:
            t = AvgMarks.objects.get(collegeId=i)
            t.academics = Reviews.objects.filter(collegeId=i, category="Academics").aggregate(Avg('marks'))['marks__avg']
            t.sports = Reviews.objects.filter(collegeId=i, category="Sports").aggregate(Avg('marks'))['marks__avg']
            t.overall = (t.academics+t.sports)/2.00
            t.save()

        self.stdout.write("Averages done!")
