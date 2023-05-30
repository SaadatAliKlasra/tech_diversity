from django.db import models
from django.urls import reverse

from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel
from tinymce.models import HTMLField

# Create your models here.


class ScholarshipCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Scholarship Categories"
        verbose_name = "Scholarship Category"
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Scholarship(TitleSlugDescriptionModel, TimeStampedModel):
    category = models.ForeignKey(ScholarshipCategory, on_delete=models.SET_NULL, null=True, blank=False)
    amount = models.CharField(max_length=100)
    deadline = models.DateField(verbose_name="Deadline")
    apply_link = models.URLField()
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("scholarship_detail_view", kwargs={"slug": self.slug})


class JobCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Job Categories"
        verbose_name = "Job Category"
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class JobType(models.TextChoices):
    PART_TIME = ("part_time", "Part Time")
    FULL_TIME = ("full_time", "Full Time")


class Job(TitleSlugDescriptionModel, TimeStampedModel):
    company_name = models.CharField(max_length=200)
    job_type = models.CharField(max_length=20, choices=JobType.choices, default=JobType.PART_TIME)
    location = models.TextField()
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True, blank=False)
    salary_min = models.IntegerField(verbose_name="Min Salery")
    salary_max = models.IntegerField(verbose_name="Max Salery")
    hours = models.IntegerField(help_text="working hours per week")
    apply_link = models.URLField()
    deadline = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("job_detail_view", kwargs={"slug": self.slug})
