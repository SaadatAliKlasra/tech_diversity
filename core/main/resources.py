from import_export import resources, fields
from import_export.widgets import DateWidget

from core.main.models import Job, JobCategory, Scholarship, ScholarshipCategory


class ScholarshipResource(resources.ModelResource):
    class Meta:
        model = Scholarship
        fields = ("title", "description", "amount", "apply_link", "deadline")
        import_id_fields = ["title"]

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        # Define a dictionary to map the new column names to the original ones
        column_name_mapping = {
            "Scholarship Name": "title",
            "Description": "description",
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
            "amount": "Amount",
            "apply_link": "Link",
            "deadline": "Deadline",
        }

        # Change the column names in the dataset headers
        dataset.headers = [column_name_mapping.get(header, header) for header in dataset.headers]

        return dataset
