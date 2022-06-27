from django.contrib import admin
from .models import Artiles, motors


class MotorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ['title']

class ArtilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'anons', 'date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'anons')
    list_filter = ('anons', 'date')

# Register your models here.
admin.site.register(Artiles, ArtilesAdmin)
admin.site.register(motors, MotorsAdmin)