from django import forms
from app.models.client_conn import Client_conn

class ClientConnForm(forms.ModelForm):
    class Meta:
        model = Client_conn
        fields = ["name", "email", "subject", "message"]
        labels = {
            "name": "First Name",
            "email": "Email Address",
            "subject": "Subject",
            "message": "Write Message..."
        }

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First Name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email Address"
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subject"
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Write Message..."
            }),
        }