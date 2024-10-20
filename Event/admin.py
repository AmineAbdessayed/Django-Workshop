from django.contrib import admin
from .models import Event



# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'evt_date', 'state', 'nbr_participant', 'creation_date', 'update_date']
    readonly_fields=['creation_date','update_date']
    list_per_page=2
    
    
    
admin.site.register(Event,EventAdmin)