from django.contrib import admin
from sites.models import *


# Register your models here.
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'contact_type', 'contact', 'sort', 'create_time')
    search_fields = ('name',)
    list_filter = ('contact_type',)
    list_editable = ('name', 'sort')
    list_per_page = 10


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_time')
    search_fields = ('title',)
    list_filter = ('published',)
    # list_editable = ('published',)
    list_per_page = 10


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort', 'url')
    list_editable = ('name', 'sort')
