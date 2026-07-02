from django import forms
from insta.models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['image', 'description']

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder':'Description'}),
        }

        labels = {
            'image': 'image',
            'description': 'description',
        }

