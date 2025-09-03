from django import forms
from .models import Feedback

class FeedbackForms(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'placeholder': 'write your feedback here....',
                'route': 4,
                'cols': 40,
            }),
        }