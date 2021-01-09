from django.contrib import admin

from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['request', 'doer']
    save_as = True
