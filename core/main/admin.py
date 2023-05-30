from django.contrib import admin

from import_export.admin import ImportExportModelAdmin


from core.main.models import Job, JobCategory, Scholarship, ScholarshipCategory
from core.main.resources import ScholarshipResource

# Register your models here.

admin.site.register((JobCategory, ScholarshipCategory))


def make_active(modeladmin, request, queryset):
    queryset.update(active=True)


make_active.short_description = "Mark selected as active"


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "created", "modified")
    list_display_links = ("title",)
    list_filter = ("category",)
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
