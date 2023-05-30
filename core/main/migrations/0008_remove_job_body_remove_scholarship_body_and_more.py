# Generated by Django 4.1.9 on 2023-05-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0007_alter_scholarship_amount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="body",
        ),
        migrations.RemoveField(
            model_name="scholarship",
            name="body",
        ),
        migrations.AlterField(
            model_name="job",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="scholarship",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="scholarship",
            name="deadline",
            field=models.DateField(verbose_name="Deadline"),
        ),
    ]
