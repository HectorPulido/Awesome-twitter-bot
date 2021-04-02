import csv
from datetime import datetime
from django.http import HttpResponse


class ExportCsvMixin:
    def export_as_csv_response(self, request, queryset):
        meta = self.model._meta
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename={}.csv".format(meta)
        writer = csv.writer(response)
        writer.writerows(ExportCsvMixin.get_data_array(queryset))
        return response

    @staticmethod
    def export_as_csv_file(queryset):
        meta = queryset.model._meta
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y%H%M%S")
        filename = f"{meta}.{dt_string}.csv"
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(ExportCsvMixin.get_data_array(queryset))
        return filename

    @staticmethod
    def get_data_array(queryset):
        arr = []
        fields = queryset.model._meta.fields
        field_names = [field.name for field in fields]
        arr.append(field_names)
        for obj in queryset:
            arr.append([getattr(obj, field) for field in field_names])
        return arr

    export_as_csv_response.short_description = "Export Selected"
