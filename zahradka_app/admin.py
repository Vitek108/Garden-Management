from django.contrib import admin
from .models import Plant, Event, TimeOfEvent, Garden, GardenPlant


class PlantAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


class TimeOfEventAdmin(admin.ModelAdmin):
    list_display = ["event", "start_date", "end_date"]


class GardenAdmin(admin.ModelAdmin):
    pass

class GardenPlantAdmin(admin.ModelAdmin):
    pass

admin.site.register(Plant, PlantAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(TimeOfEvent, TimeOfEventAdmin)
admin.site.register(Garden, GardenAdmin)
admin.site.register(GardenPlant, GardenPlantAdmin)
