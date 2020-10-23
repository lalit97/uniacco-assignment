import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import UserLoginHistory


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = queryset.model._meta
        field_names = [field.name for field in meta.fields]
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=UserLoginHistory.csv'
        
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in reversed(queryset):
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = "Export Selected as csv"


class UserLoginHistoryAdmin(admin.ModelAdmin, ExportCsvMixin):
    actions = ['export_as_csv']

admin.site.register(UserLoginHistory, UserLoginHistoryAdmin)
