from django.db import models
from django.contrib import admin
from capturing.models import NewSites, TextSite
from django.contrib.auth.models import User

class NewSiteAdmin(admin.ModelAdmin):
    fieldsets = (
            ('added data', {
                'fields': ('url',
                           'user',
                           )
            }),            
    )
    list_filter   = ('url', 'user')
    list_display  = ('url', 'user')
    search_fields = ('url', 'user')

class TextSiteAdmin(admin.ModelAdmin):
    fieldsets = (
            ('text', {
                'fields': ('url',
                           'title',
                           'text',
                           'site',
                           )
            }),            
    )

    list_filter   = ('url',)
    list_display  = ('url', 'title')
    search_fields = ('url', 'title')

admin.site.register(NewSites, NewSiteAdmin)
admin.site.register(TextSite, TextSiteAdmin)
