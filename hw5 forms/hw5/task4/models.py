from django.db import models
from django.urls import reverse


class Review(models.Model):
    """Review model"""

    CHOICE_SCORE = ((1, 'Really bad'),
                    (2, 'Bad'),
                    (3, 'Normal'),
                    (4, 'Well'),
                    (5, 'Perfect'))

    email = models.EmailField(max_length=70)
    content = models.TextField(blank=True, max_length=200, null=True)
    photo = models.ImageField(upload_to="task4/media/photos/%Y/%m/%d/", blank=True, null=True)
    score = models.IntegerField(default=3, choices=CHOICE_SCORE)
    phone = models.CharField(max_length=15, null=True, blank=True)
    is_positive = models.BooleanField(default=True, verbose_name='Is it positive review')
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email}: score={self.score}'

    def get_absolute_url(self):
        return reverse('review', kwargs={"review_pk": self.pk})

    class Meta:
        ordering = ['-time_create']
