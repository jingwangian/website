from django.contrib import admin

# Register your models here.
from .models import EC2Info

admin.site.register(EC2Info)
