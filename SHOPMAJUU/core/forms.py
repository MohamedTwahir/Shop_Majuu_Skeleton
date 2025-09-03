from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
        "phone",
        "address_line1",
        "address_line2",
        "city",
        "state",
        "postal_code",
        "country",
        ]


class TrackingForm(forms.Form):
    tracking_number = forms.CharField(max_length=20)