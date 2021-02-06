from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import *


class DoerRequestInline(admin.StackedInline):
    extra = 0
    model = DoerRequest


@admin.register(DoerRequest)
class DoerRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(OSMGeoAdmin):
    list_display = ['request', ]
    readonly_fields = ['doer']
    inlines = [DoerRequestInline, ]
    save_as = True
