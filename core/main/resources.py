import re

from django.core.exceptions import ObjectDoesNotExist

from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from core.main.models import Job, Scholarship, ScholarshipCategory


class ScholarshipResource(resources.ModelResource):
    category = fields.Field(
        column_name="category", attribute="category", widget=ForeignKeyWidget(ScholarshipCategory, "name")
    )  # assuming the 'name' is the unique identifier of your category

    class Meta:
        model = Scholarship
        fields = ("title", "description", "category", "amount", "apply_link", "deadline")
        import_id_fields = ["title"]

    def before_import_row(self, row, **kwargs):
        category_name = row.get("category")
        if category_name:
            try:
                category = ScholarshipCategory.objects.get(name=category_name)
                row["Category"] = category.pk
            except ObjectDoesNotExist:
                category = ScholarshipCategory.objects.create(name=category_name)
                row["Category"] = category.pk

        # Remove "$" and "," from the "amount" field
        amount = row.get("amount")
        if amount:
            row["amount"] = re.sub(r"[$,]", "", amount)

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        # Define a dictionary to map the new column names to the original ones
        column_name_mapping = {
            "Scholarship Name": "title",
            "Description": "description",
            "Category": "category",
            "Amount": "amount",
            "Link": "apply_link",
            "Deadline": "deadline",
        }

        # Change the column names in the dataset headers
        dataset.headers = [column_name_mapping.get(header, header) for header in dataset.headers]

    def export(self, queryset=None, *args, **kwargs):
        dataset = super().export(queryset, *args, **kwargs)

        # Define a dictionary to map the original column names to the new ones
        column_name_mapping = {
            "title": "Scholarship Name",
            "description": "Description",
            "category": "Category",
            "amount": "Amount",
            "apply_link": "Link",
            "deadline": "Deadline",
        }

        # Change the column names in the dataset headers
        dataset.headers = [column_name_mapping.get(header, header) for header in dataset.headers]

        return dataset


class JobResource(resources.ModelResource):
    class Meta:
        model = Job
        fields = (
            "title",
            "company_name",
            "salary_range",
            "posted",
            "job_type",
            "location",
            "description",
            "full_job_description",
            "apply_link",
        )
        import_id_fields = ["title"]

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        # Define a dictionary to map the new column names to the original ones
        column_name_mapping = {
            "Job Title": "title",
            "Company Name": "company_name",
            "Salary Range": "salary_range",
            "Posted": "posted",
            "Job Type": "job_type",
            "Location": "location",
            "Brief Job Description": "description",
            "Full Job Description": "full_job_description",
            "Link": "apply_link",
        }

        # Change the column names in the dataset headers
        dataset.headers = [column_name_mapping.get(header, header) for header in dataset.headers]

    def export(self, queryset=None, *args, **kwargs):
        dataset = super().export(queryset, *args, **kwargs)

        # Define a dictionary to map the original column names to the new ones
        column_name_mapping = {
            "title": "Job Title",
            "company_name": "Company Name",
            "salary_range": "Salary Range",
            "posted": "Posted",
            "expiration_date": "Expiration Date",
            "job_type": "Job Type",
            "location": "Location",
            "description": "Brief Job Description",
            "full_job_description": "Full Job Description",
            "apply_link": "Link",
        }

        # Change the column names in the dataset headers
        dataset.headers = [column_name_mapping.get(header, header) for header in dataset.headers]

        return dataset
