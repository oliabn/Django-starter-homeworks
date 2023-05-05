from django.db import models
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField
"""How to set PhoneNumberField
    1) pip install django-phonenumber-field
    2) in settings.py: INSTALLED_APPS = [..., 'phonenumber_field',] 
    3) in models.py: from phonenumber_field.modelfields import PhoneNumberField
    4) in model class: phone = PhoneNumberField()"""


class Review(models.Model):
    """Review model"""

    CHOICE_SCORE = ((1, 'Really bad'),
                    (2, 'Bad'),
                    (3, 'Normal'),
                    (4, 'Well'),
                    (5, 'Perfect'))

    email = models.EmailField(max_length=70, unique=True)
    content = models.TextField(blank=True, max_length=200, null=True, default=None)
    photo = models.ImageField(upload_to="task4/media/photos/%Y/%m/%d/", blank=True, null=True)
    score = models.IntegerField(default=3, choices=CHOICE_SCORE)
    phone = PhoneNumberField(blank=True, null=True, default=None)
    # phone = models.CharField(max_length=12, null=True, blank=True)
    is_positive = models.BooleanField(default=True, verbose_name='Is it positive review')
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email}: score={self.score}'

    def get_absolute_url(self):
        return reverse('review', kwargs={"review_pk": self.pk})

    class Meta:
        ordering = ['-time_create']
