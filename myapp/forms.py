from django import forms
from .models import Appointment, ContactMessage


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "fullName",
            "email",
            "phoneNumber",
            "department",
            "date",
            "message",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "message": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["fullName", "email", "phoneNumber", "subject", "message"]
        widgets = {
            "fullName": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your Name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Your Email",
            }),
            "phoneNumber": forms.TextInput(attrs={
                "class": "form-control",
                "type": "tel",
                "placeholder": "Your Phone (optional)",
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subject",
            }),
            "message": forms.Textarea(attrs={
                "rows": 6,
                "class": "form-control",
                "placeholder": "Your Message",
            }),
        }