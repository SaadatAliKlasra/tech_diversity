# Generated by Django 4.1.9 on 2023-06-08 05:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0024_rename_deadline_job_expiration_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="expiration_date",
        ),
    ]
