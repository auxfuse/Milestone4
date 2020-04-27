from django import forms
from .models import Order
from checkout.choices import months, years


class MakePaymentForm(forms.Form):

    credit_card_number = forms.CharField(
        min_length=15,
        max_length=16,
        required=False,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Credit Card Number'
        })
    )

    cvv = forms.CharField(
        min_length=1,
        max_length=3,
        required=False,
        label='',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Security Code (CVV)',
            'required': 'True'
        })
    )

    expiry_month = forms.ChoiceField(
        required=False,
        label='',
        choices=months,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    expiry_year = forms.ChoiceField(
        required=False,
        label='',
        choices=years,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    stripe_id = forms.CharField(
        widget=forms.HiddenInput
    )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = {
            'full_name',
            'email'
        }

    full_name = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Full Name',
            'autofocus': 'True'
        })
    )

    email = forms.EmailField(
        required=True,
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email'
        })
    )
