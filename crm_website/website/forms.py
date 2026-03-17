from django import forms
from .models import Record

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    city = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    address = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    email = forms.EmailField(   
        required=True,
        widget=forms.EmailInput(attrs={

            'class': 'form-control'
        })
    )

    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={

            'class': 'form-control'
        })
    )

    state = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={

            'class': 'form-control'
        })
    )

    zip_code = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={

            'class': 'form-control'
        })
    )

    class Meta:
        model = Record
        exclude = ("user",)