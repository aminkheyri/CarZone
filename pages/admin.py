from django.contrib import admin
from .models import Teams
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;"/>'.format(object.photo.url))

    thumbnail.short_description = 'photo'

    list_display = ('id', 'thumbnail', 'last_name', 'designation', 'created_date')
    list_display_links = ('id', 'thumbnail', 'last_name',)
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)


admin.site.register(Teams, TeamAdmin)