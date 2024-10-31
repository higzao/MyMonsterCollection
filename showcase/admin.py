from django.contrib import admin
from showcase.models import Can

class ListCans(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )

admin.site.register(Can, ListCans)