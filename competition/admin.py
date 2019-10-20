from django.contrib import admin
from .models import *
import csv
from django.http import HttpResponse


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
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"
    
    actions = ["export_as_csv"]