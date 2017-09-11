from django.contrib import admin

# Register your models here.
from .models import EC2Info
# from .models import City,Route,RouteTask,RouteTaskHistory

admin.site.register(EC2Info)
# admin.site.register(City)
# admin.site.register(Route)
# admin.site.register(RouteTask)
# admin.site.register(RouteTaskHistory)
