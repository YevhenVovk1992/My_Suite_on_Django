from django.contrib import admin
from .models import Artiles, motors


class MotorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ['title']

# Register your models here.
admin.site.register(Artiles)
admin.site.register(motors, MotorsAdmin)