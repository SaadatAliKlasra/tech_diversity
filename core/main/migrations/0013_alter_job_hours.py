# Generated by Django 4.1.9 on 2023-06-06 13:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0012_remove_job_salary_max_remove_job_salary_min_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="hours",
            field=models.IntegerField(blank=True, help_text="working hours per week", null=True),
        ),
    ]