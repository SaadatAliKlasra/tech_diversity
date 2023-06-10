from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML
import django_filters

from core.main.models import Job, Scholarship


class ScholarshipFilter(django_filters.FilterSet):
    deadline = django_filters.DateFilter(
        field_name="deadline",
        lookup_expr="lte",
        label="Deadline",
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    amount = django_filters.CharFilter(
        field_name="amount",
        label="Amount",
        lookup_expr="iexact",
        widget=forms.TextInput(attrs={"placeholder": "Enter amount"}),
    )

    class Meta:
        model = Scholarship
        fields = ("category", "amount", "deadline")


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name="title",
        label="Job Title",
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"placeholder": "Enter Title"}),
    )
    location = django_filters.CharFilter(
        field_name="location",
        label="Location",
        lookup_expr="icontains",
        widget=forms.TextInput(attrs={"placeholder": "Enter a location"}),
    )

    class Meta:
        model = Job
        fields = ["title", "location", "job_type"]
