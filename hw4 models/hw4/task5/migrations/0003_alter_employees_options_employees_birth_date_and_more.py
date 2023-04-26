# Generated by Django 4.2 on 2023-04-25 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task5', '0002_alter_department_dep_name_alter_employees_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employees',
            options={'ordering': ('department', 'first_name')},
        ),
        migrations.AddField(
            model_name='employees',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='hire_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='dep_name',
            field=models.CharField(max_length=100, null=True, verbose_name='department'),
        ),
    ]
