from django.contrib import admin

from .models import City,Route,RouteTask,RouteTaskHistory
# Register your models here.

admin.site.register(City)
admin.site.register(Route)
admin.site.register(RouteTask)
admin.site.register(RouteTaskHistory)
