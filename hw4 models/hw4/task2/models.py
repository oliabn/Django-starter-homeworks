from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        ordering = ('surname', )


class Book(models.Model):
    CHOICE_GENRE = (('fantasy', 'fantasy'),
                    ('comedy', 'comedy'),
                    ('drama', 'drama'),
                    ('horror', 'horror'),
                    ('popular science', 'popular science'))

    name = models.CharField(max_length=80)
    authors = models.ManyToManyField(Author)
    genre = models.CharField(max_length=50, choices=CHOICE_GENRE)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
