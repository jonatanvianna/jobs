from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        help_texts = {
            "title": "The Job position you are creating.",
            "description": "Fill the Job details, like tasks and skills.",
            "company": "The company that is offering the position.",
            "email": "The email contat for the candidates.",

            }
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Python developer", "class": "input"}
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "ACME Company is looking for a Python developer ....",
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
