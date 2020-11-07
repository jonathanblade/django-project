from django.contrib import admin

from publications.models import Publication

class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'year']

admin.site.register(Publication, PublicationAdmin)