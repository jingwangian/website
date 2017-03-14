from django.contrib import admin

# Register your models here.
from .models import FlightPriceQueryTask
from .models import FlightTaskStatus

admin.site.register(FlightPriceQueryTask)
admin.site.register(FlightTaskStatus)