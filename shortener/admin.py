from django.contrib import admin

from .models import KirrURL


class KirrURLAdmin(admin.ModelAdmin):
    list_display = ['shortcode', 'url']

admin.site.register(KirrURL, KirrURLAdmin)
