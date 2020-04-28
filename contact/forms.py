from django import forms
from .models import Contact


class ContactQuery(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'query_title',
            'query_text',
            'query_email'
        ]

    query_title = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Query Title'
        })
    )
    query_text = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Query Details'
        })
    )
    query_email = forms.EmailField(
        required=True,
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Email'
        })
    )
