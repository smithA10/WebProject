from django.contrib import admin
from .models import VehicleDetail,VehicleMake,OwnerProfile

# Register your models here.
admin.site.register(VehicleDetail)
admin.site.register(VehicleMake)
admin.site.register(OwnerProfile)