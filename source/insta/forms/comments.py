from django import forms
from insta.models import Comments

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']

        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'rows': 3, 'placeholder':'Comment'}),
        }

        labels = {
            'text': '',
        }