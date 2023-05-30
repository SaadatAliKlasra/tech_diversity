from django.shortcuts import render
from django.views.generic import DetailView
from django_filters.views import FilterView
from core.main.models import Scholarship, Job
from core.main.filters import ScholarshipFilter, JobFilter

# Create your views here.


class ScholarshipListView(FilterView):
    model = Scholarship
    template_name = "pages/scholarship.html"
    filterset_class = ScholarshipFilter
    paginate_by = 20
    queryset = Scholarship.objects.filter(active=True)


class ScholarshipDetailView(DetailView):
    model = Scholarship
    template_name = "pages/scholarship_detail.html"
    queryset = Scholarship.objects.filter(active=True)
    slug_field = "slug"
    slug_url_kwarg = "slug"


class JobListView(FilterView):
    model = Job
    template_name = "pages/job_search.html"
    filterset_class = JobFilter
    paginate_by = 20
    queryset = Job.objects.filter(active=True)


class JobDetailView(DetailView):
    model = Job
    template_name = "pages/job_detail.html"
    queryset = Job.objects.filter(active=True)
    slug_field = "slug"
    slug_url_kwarg = "slug"
