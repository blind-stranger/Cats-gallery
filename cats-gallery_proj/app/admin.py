from django.contrib import admin
from app.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'priority', 'thumbnail']
    list_editable = ['priority', 'thumbnail']


admin.site.register(Photo, PhotoAdmin)
