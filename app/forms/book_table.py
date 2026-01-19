from django import forms
from app.models.book_table import BookTable, BookBusinessTable

class BookTableForm(forms.ModelForm):
    class Meta:
        model = BookTable
        fields = ["name", "email", "phone", "guest_choice", "date", "time", "requests"]

        labels = {
            "name": "Your Name",
            "email": "Your Email", 
            "phone": "Your Phone",
            "guest_choice": "Number of Guests",
            "date": "Date",
            "time": "Time", 
            "requests": "Special requests or dietary restrictions"
        }
        
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Name",
                "required": True
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control", 
                "placeholder": "Your Email",
                "required": True
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Phone", 
                "required": True
            }),
            "guest_choice": forms.Select(attrs={
                "class": "form-control",
                "required": True
            }),
            "date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control",
                "required": True
            }),
            "time": forms.TimeInput(attrs={
                "type": "time", 
                "class": "form-control",
                "required": True
            }),
            "requests": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Special requests or dietary restrictions"
            })
        }

class BookBusinessTableForm(forms.ModelForm):
    class Meta:
        model = BookBusinessTable
        fields = ["name", "email", "phone", "guest_choice", "date", "time", "requests", "occasions"]
        
        labels = {
            "name": "Your Name",
            "email": "Your Email", 
            "phone": "Your Phone",
            "guest_choice": "Number of Guests",
            "date": "Date",
            "time": "Time", 
            "requests": "Special requests or dietary restrictions",
            "occasions": "Special occasion for book table"
        }
        
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Name",
                "required": True
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control", 
                "placeholder": "Your Email",
                "required": True
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Phone", 
                "required": True
            }),
            "guest_choice": forms.Select(attrs={
                "class": "form-control",
                "required": True
            }),
            "date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control",
                "required": True
            }),
            "time": forms.TimeInput(attrs={
                "type": "time", 
                "class": "form-control",
                "required": True
            }),
            "requests": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Special requests or dietary restrictions"
            }),
            "occasions": forms.Select(attrs={
                "class": "form-control",
                "placeholder": "Special occasion for book table",
                "required": True
            })
        }
