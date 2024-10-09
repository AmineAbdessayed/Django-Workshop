from django.contrib import admin
from .models import Person
# Register your models here.


class ResearchPerson(admin.ModelAdmin):
    search_fields = ['username']

admin.site.register(Person, ResearchPerson)
