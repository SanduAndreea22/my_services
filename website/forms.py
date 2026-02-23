from django import forms
from .models import ContactMessage


class StartProjectForm(forms.ModelForm):

    FEATURE_CHOICES = [
        ("stripe", "Stripe Payment Integration"),
        ("charts", "Interactive Charts / Data Visualization"),
        ("custom_admin", "Custom Admin Panel Management"),
        ("none", "None of the above"),
    ]

    required_features = forms.MultipleChoiceField(
        choices=FEATURE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = ContactMessage
        fields = [
            "name",
            "email",
            "industry",
            "project_description",
            "hosting_info",
            "deadline_communication",
            "required_features",
        ]

from django import forms
from .models import ContactMessageSimple


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessageSimple
        fields = ["name", "email", "message"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full p-3 rounded-lg bg-slate-800 border border-slate-700 text-white"
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full p-3 rounded-lg bg-slate-800 border border-slate-700 text-white"
            }),
            "message": forms.Textarea(attrs={
                "rows": 5,
                "class": "w-full p-3 rounded-lg bg-slate-800 border border-slate-700 text-white"
            }),
        }