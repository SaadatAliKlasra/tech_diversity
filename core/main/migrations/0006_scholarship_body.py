# Generated by Django 4.1.9 on 2023-05-23 17:34

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_job_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="scholarship",
            name="body",
            field=tinymce.models.HTMLField(default="dsas"),
            preserve_default=False,
        ),
    ]
