from django.contrib import admin

from .models import *


class DoerRequestInline(admin.StackedInline):
    extra = 0
    model = DoerRequest


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['request', ]
    readonly_fields = ['doer']
    inlines = [DoerRequestInline, ]
    save_as = True
