from django import forms
from django.core.exceptions import ValidationError

from .models import *


class ArticleAddingForm(forms.ModelForm):
    """Article adding form.
    The class is related to the Article model.
    Authorization Form for task3"""
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    class Meta:
        model = Article
        fields = ['title', 'slug', 'content', 'photo', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean(self):
        data = self.cleaned_data

        # title validation
        title = data.get('title')
        # get title from Article table
        qs = Article.objects.all().filter(title__icontains=title)
        # Checking if the title already exists. Not accept already existing title
        if qs.exists():
            self.add_error('title', f'<{title}> is already in use. Please change title')
        if len(title) > 100:
            raise ValidationError('Title is to long')

        # slug validation
        slug = data.get('slug')
        # get all slugs from Article table
        qs = Article.objects.all().filter(slug__icontains=slug)
        # Checking if the slug already exists. Not accept already existing slug
        if qs.exists():
            self.add_error('slug', f'<{slug}> is already in use. Please change URL')

        return data
