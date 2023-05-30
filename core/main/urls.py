from django.urls import path
from django.views.generic import TemplateView

from core.main import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("our-team/", TemplateView.as_view(template_name="pages/our_team.html"), name="our_team"),
    path("our-mission/", TemplateView.as_view(template_name="pages/our_mission.html"), name="our_mission"),
    path("our-scholarship/", TemplateView.as_view(template_name="pages/our_scholarship.html"), name="our_scholarship"),
    path("donate/", TemplateView.as_view(template_name="pages/donate.html"), name="donate"),
    path("partner/", TemplateView.as_view(template_name="pages/partner.html"), name="partner"),
    path("contact/", TemplateView.as_view(template_name="pages/contact.html"), name="contact"),
    path("scholarship/", views.ScholarshipListView.as_view(), name="scholarship_list_view"),
    path("scholarship/<slug:slug>/", views.ScholarshipDetailView.as_view(), name="scholarship_detail_view"),
    path("job/", views.JobListView.as_view(), name="job_list_view"),
    path("job/<slug:slug>/", views.JobDetailView.as_view(), name="job_detail_view"),
]
