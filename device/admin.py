from django.contrib import admin
from device.models import *


# Register your models here.

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'device_no', 'type', 'create_date')
    list_filter = ('type',)
    search_fields = ('name',)


@admin.register(Firmware)
class FirmwareAdmin(admin.ModelAdmin):
    list_filter = ('id', 'device', 'identifier', 'version', 'url', 'releasedate', 'uploaddate', 'signed', 'create_date')
    list_filter = ('device', 'signed')
    search_fields = ('version',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'update_date', 'file')
