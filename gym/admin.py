from django.contrib import admin
from .models import *


class SuplementAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'image', 'cat')
    list_display_links = ('name',)
    search_fields = ('name', 'content', 'cat')


admin.site.register(Team)
admin.site.register(Suplement, SuplementAdmin)
admin.site.register(Category)
