# Generated by Django 4.2 on 2023-04-23 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task4', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('zipcode', models.CharField(max_length=200, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task4.customer')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task4.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='task4.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='task4.product')),
            ],
        ),
    ]
