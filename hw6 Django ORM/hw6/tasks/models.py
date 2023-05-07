from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        ordering = ('surname',)


class Book(models.Model):
    CHOICE_GENRE = (('fantasy', 'fantasy'),
                    ('comedy', 'comedy'),
                    ('drama', 'drama'),
                    ('horror', 'horror'),
                    ('popular science', 'popular science'))

    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=80)
    genre = models.CharField(max_length=50, choices=CHOICE_GENRE)
    description = models.TextField(max_length=1000)
    pub_date = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
