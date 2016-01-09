from django.contrib import admin
from .models import College, Academics, Sports

# Register your models here.

class AcademicsInline(admin.StackedInline):
    model = Academics
    extra = 1

class SportsInline(admin.StackedInline):
    model = Sports
    extra = 1

class CollegeAdmin(admin.ModelAdmin):
    inlines = [AcademicsInline, SportsInline]
    list_display = ('name', 'university', 'location', 'phone', 'email', 'datePublished')
    list_filter = ['university','location']
    search_fields = ['name', 'university']


admin.site.register(College,CollegeAdmin)
