from django import forms
from django.core.exceptions import ValidationError

from .models import *


class ReviewAddingForm(forms.ModelForm):
    """Review adding form.
    The class is related to the Review model."""

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    class Meta:
        model = Review
        fields = ['email', 'content', 'photo', 'score', 'phone', 'is_positive']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
