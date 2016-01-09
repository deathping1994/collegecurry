from django.contrib import admin
from reviews.models import Reviews

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('dateAdded','collegeId', 'category', 'marks', 'authorName', 'authorYear', 'authorEmail', 'authorCourse')
    list_filter = ['marks', 'category']
    search_fields = ['authorName', 'catgory', 'collegeId']

admin.site.register(Reviews, ReviewAdmin)
