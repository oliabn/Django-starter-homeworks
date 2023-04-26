from django.db import models


class Customer(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    user_uuid = models.UUIDField()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('surname', 'name',)
        # app_label = 'task6'


class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    is_available = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('is_available', 'name',)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'oder {self.id}, customer: {self.customer.email}'
