from django.contrib import admin
from application.models import *
from .resources import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class RestaurantAdmin(ImportExportModelAdmin):
    resource_class = RestaurantResource


admin.site.register(Restaurant, RestaurantAdmin)
