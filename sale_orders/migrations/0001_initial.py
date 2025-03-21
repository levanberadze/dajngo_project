# Generated by Django 5.1.7 on 2025-03-17 15:23

import django.db.models.deletion
import sale_orders.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('write_date', models.DateTimeField(auto_now_add=True)),
                ('archived', models.BooleanField(default=False)),
                ('name', models.CharField(default=sale_orders.models.generate_sale_name, editable=False, max_length=250, unique=True)),
                ('completed', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SaleOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('write_date', models.DateTimeField(auto_now_add=True)),
                ('archived', models.BooleanField(default=False)),
                ('qty', models.PositiveIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='sale_orders.saleorder')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
