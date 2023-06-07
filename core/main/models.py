from django.db import models
from django.urls import reverse

from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel
from tinymce.models import HTMLField

# Create your models here.


class ScholarshipCategory(models.Model):
    name = models.CharField(max_length=300, unique=True)

    class Meta:
        verbose_name_plural = "Scholarship Categories"
        verbose_name = "Scholarship Category"
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Scholarship(TitleSlugDescriptionModel, TimeStampedModel):
    category = models.ForeignKey(ScholarshipCategory, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.CharField(max_length=100)
    deadline = models.DateField(verbose_name="Deadline")
    apply_link = models.URLField()
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("scholarship_detail_view", kwargs={"slug": self.slug})


# class JobCategory(models.Model):
#     name = models.CharField(max_length=300, unique=True)

#     class Meta:
#         verbose_name_plural = "Job Categories"
#         verbose_name = "Job Category"
#         ordering = ("name",)

#     def __str__(self) -> str:
#         return self.name


class JobType(models.TextChoices):
    PART_TIME = ("Part-time", "Part-time")
    FULL_TIME = ("Full-time", "Full-time")


class Job(TitleSlugDescriptionModel):
    company_name = models.CharField(max_length=300, null=True, blank=True)
    job_type = models.CharField(max_length=20, choices=JobType.choices, default=JobType.PART_TIME)
    location = models.TextField(null=True, blank=True)
    salary_range = models.CharField(max_length=300, verbose_name="Salary Range")
    full_job_description = models.TextField(null=True, blank=True)
    hours = models.IntegerField(help_text="working hours per week", null=True, blank=True)
    apply_link = models.CharField(max_length=1000)
    deadline = models.DateField(null=True, blank=True)
    posted = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("job_detail_view", kwargs={"slug": self.slug})
