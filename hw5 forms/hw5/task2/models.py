from django.db import models


class User(models.Model):
    """User Model"""

    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']
