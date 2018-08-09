from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Python developer", "class": "input"}
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Some Job description",
                    "class": "textarea",
                }
            ),
            "company": forms.TextInput(
                attrs={"placeholder": "Acme inc.", "class": "input"}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "jobs@acme.inc", "class": "input"}
            ),
        }
