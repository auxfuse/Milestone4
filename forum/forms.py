from django import forms
from .models import Post, PostComment


class CreatePost(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget.attrs['class'] = 'form-control'
        self.fields['category'].label = ''
        self.fields['category'].required = True

    class Meta:
        model = Post
        fields = [
            'title',
            'post_text',
            'category'
        ]

    title = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Post Title'
        })
    )
    post_text = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Add your Post Details'
        })
    )


class CreateComment(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = [
            'comment_text'
        ]

    comment_text = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'rows': 2,
            'class': 'form-control',
            'placeholder': 'Add your Comment Details'
        })
    )