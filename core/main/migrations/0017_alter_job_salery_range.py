# Generated by Django 4.1.9 on 2023-06-07 08:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0016_alter_job_company_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="salery_range",
            field=models.CharField(max_length=300, verbose_name="Salery Range"),
        ),
    ]
