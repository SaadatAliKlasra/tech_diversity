# Generated by Django 4.1.9 on 2023-06-07 08:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0014_job_full_job_description_alter_job_job_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="category",
        ),
        migrations.RemoveField(
            model_name="job",
            name="created",
        ),
        migrations.RemoveField(
            model_name="job",
            name="modified",
        ),
        migrations.AddField(
            model_name="job",
            name="posted",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="company_name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="deadline",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="location",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name="JobCategory",
        ),
    ]