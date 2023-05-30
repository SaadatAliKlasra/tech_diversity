from django import forms

import django_filters

from core.main.models import Job, Scholarship


class ScholarshipFilter(django_filters.FilterSet):
    deadline = django_filters.DateFilter(
        field_name="deadline", lookup_expr="gte", label="Deadline", widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Scholarship
        fields = ["category", "amount", "deadline"]


class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = ["title", "location", "category", "job_type"]
