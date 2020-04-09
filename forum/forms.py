from django import forms
from .models import Post


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'post',
            'categories'
        ]

    title = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Post Title'
        })
    )
    post = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Add your Post Details'
        })
    )
    categories = forms.ChoiceField(
        required=True,
        label='',
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
