from unicodedata import name
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("id", "name", "url")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_image")
    list_display_links = ("id", "name", "get_image")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width="60" height="100%"/>')


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand")
    list_display_links = ("id", "name", "brand")
    list_filter = ("brand",)

@admin.register(DriveUnit)
class DriveUnitAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")

@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")


@admin.register(BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")

@admin.register(EngineCapacity)
class EngineCapacityAdmin(admin.ModelAdmin):
    list_display = ("id", "capacity")
    list_display_links = ("id", "capacity")

@admin.register(SteeringWheel)
class SteeringWheelAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")

@admin.register(Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', "category", "brand", "carModel", 'steeringWheel', 'year_of_issue', 'created_at')
    list_display_links = ("id", "category", "brand", "carModel")