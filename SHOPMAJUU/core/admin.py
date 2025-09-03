from django.contrib import admin
from .models import Warehouse, UserProfile, Package, TrackingEvent, Invoice

# Register your models here.

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ("code", "city", "country")


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "customer_code", "assigned_warehouse")


class TrackingEventInline(admin.TabularInline):
    model = TrackingEvent
    extra = 0


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("tracking_number", "user", "warehouse", "status", "weight_kg")
    inlines = [TrackingEventInline]


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("package", "amount", "currency", "paid")