from django.db import models


class Department(models.Model):
    dep_name = models.CharField(max_length=100, null=True, verbose_name='department')

    def __str__(self):
        return self.dep_name


class Employees(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    birth_date = models.DateField(auto_now=False, null=True, blank=True)
    hire_date = models.DateField(auto_now=False, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} from {self.department}'

    class Meta:
        ordering = ('department', 'first_name',)
