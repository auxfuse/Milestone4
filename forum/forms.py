from django import forms
from .models import Post


class CreatePost(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].widget.attrs['class'] = 'form-control'
        self.fields['categories'].label = ''
        self.fields['categories'].required = True

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
