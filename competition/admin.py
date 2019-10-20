from django.contrib import admin
from .models import *


admin.site.register(Group)
admin.site.register(HappyHour)
admin.site.register(University)
admin.site.register(GroupScore)
admin.site.register(Criterium)

@admin.register(Runner)
class RunnerAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']

@admin.register(Lap)
class LapAdmin(admin.ModelAdmin):
    search_fields = ['runner__first_name', 'runner__last_name']
