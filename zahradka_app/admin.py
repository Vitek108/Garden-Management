from django.contrib import admin
from .models import Plant, Event, TimeOfEvent, Garden


class PlantAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


class TimeOfEventAdmin(admin.ModelAdmin):
    pass


class GardenAdmin(admin.ModelAdmin):
    pass


admin.site.register(Plant, PlantAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(TimeOfEvent, TimeOfEventAdmin)
admin.site.register(Garden, GardenAdmin)
