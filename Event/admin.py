from django.contrib import admin
from .models import Event



# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display=['title','evt_date','state','nbr_participant']
    
    
    
admin.site.register(Event,EventAdmin)