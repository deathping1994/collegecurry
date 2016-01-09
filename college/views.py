from django.shortcuts import render
from django.db.models import Avg
from django.utils import timezone
from .models import College, AvgMarks
from reviews.models import Reviews
from .forms import ReviewForm
# Create your views here.

def getReviews(category, id):
    if category == "all":
        reviews = Reviews.objects.filter(collegeId=id)
    else:
        reviews = Reviews.objects.filter(category=category, collegeId=id)
    return reviews

def computeGrade(points):
    if points > 1 and points <= 1.5:
        return "D-"
    elif points >1.5 and points<=2:
        return "D"
    elif points >2 and points <=2.5:
        return "D+"
    elif points >2.5 and points <=3:
        return "C"
    elif points > 3 and points <= 3.5:
        return "C+"
    elif points >3.5 and points <=4:
        return "B"
    elif points >4 and points <=4.5:
        return "B+"
    elif points>4.5 and points <= 4.65:
        return "A"
    elif points>4.65 and points <=5.00:
        return "A+"

def index(request):
    collegeList = College.objects.all()
    title = "Home"
    return render(request, "college/index.html", {
    "title":title,
    "colleges":collegeList,
    })

def collegeView(request, id):
    message=""
    college = College.objects.get(pk=id)
    title = college.name
    reviews = getReviews("all",id)
    grade = computeGrade(AvgMarks.objects.get(collegeId=id).overall)
    avg = Reviews.objects.filter(collegeId=College.objects.get(pk=id), category="Academics").aggregate(Avg('marks'))['marks__avg']

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            message = "Form entered correctly!"
            name = form.cleaned_data["authorName"]
            email = form.cleaned_data["authorEmail"]
            year = form.cleaned_data["authorYear"]
            category = form.cleaned_data["category"]
            course = form.cleaned_data["authorCourse"]
            marks = form.cleaned_data["marks"]
            review = form.cleaned_data["review"]
            r = Reviews(collegeId=college, authorName=name, authorEmail=email, authorYear=year,
            authorCourse=course, category=category, marks=marks, review=review)
            r.save()
        else:
            message = "Wrong data entered!"
    else:
        form = ReviewForm()

    return render(request, "college/collegeView.html", {
    "college":college, "title":title, "reviews":reviews, "grade":grade, "marks":avg, "message":message, "form":form,
    })

def academicsView(request, id):
    college = College.objects.get(pk=id)
    reviews = getReviews("Academics", id)
    grade = computeGrade(AvgMarks.objects.get(collegeId=id).academics)
    return render(request, "college/academicsView.html", {
    "college":college, "reviews":reviews, "grade":grade,
    })
