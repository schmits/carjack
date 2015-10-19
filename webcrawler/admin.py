from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Brand
from .models import Car


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car)
