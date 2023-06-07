from django.contrib import admin

from import_export.admin import ImportExportModelAdmin


from core.main.models import Job, Scholarship, ScholarshipCategory
from core.main.resources import ScholarshipResource, JobResource

# Register your models here.

admin.site.register(ScholarshipCategory)


def make_active(modeladmin, request, queryset):
    queryset.update(active=True)


make_active.short_description = "Mark selected as active"


@admin.register(Job)
class JobAdmin(ImportExportModelAdmin):
    resource_class = JobResource
    list_display = ("id", "title", "posted")
    list_display_links = ("title",)
    search_fields = ("title", "description")
    actions = [make_active]


@admin.register(Scholarship)
class ScholarshipAdmin(ImportExportModelAdmin):
    resource_class = ScholarshipResource
    list_display = ("id", "title", "category", "created", "modified")
    list_display_links = ("title",)
    list_filter = ("category",)
    search_fields = ("title", "description")
    actions = [make_active]
