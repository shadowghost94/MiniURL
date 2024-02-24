from django.contrib import admin
from .models import MiniURL

class MiniURLAdmin(admin.ModelAdmin):
    list_display = ('urlLongue', 'code', 'date', 'pseudo', 'nb_acces')
    list_filter = ('pseudo', )
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('urlLongue',)

admin.site.register(MiniURL, MiniURLAdmin)