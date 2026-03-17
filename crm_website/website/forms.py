from django import forms
from .models import Record
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True , widget= forms.widgets.TextInput(attrs={'placeholder': "First Name"}))
    last_name =  forms.CharField(required=True , widget= forms.widgets.TextInput(attrs={'placeholder': "last Name"}))
    city =   forms.CharField(required=True , widget= forms.widgets.TextInput(attrs={'placeholder': "city  "}))
    address = forms.CharField(required=True , widget= forms.widgets.TextInput(attrs={'placeholder': "address"}))
    email = forms.CharField(required=True , widget= forms.widgets.TextInput(attrs={'placeholder': "email"}))
    phone = forms.CharField(required=True , widget= forms.widgets.TextInput(attrs={'placeholder': "phone"}))
    state = forms.CharField(required=True , widget= forms.widgets.TextInput(attrs={'placeholder': "state"}))
    zip_code = forms.CharField(required=True , widget= forms.widgets.TextInput(attrs={'placeholder': "zip code"}))

    class Meta:
        model = Record
        exclude = ("user", )

