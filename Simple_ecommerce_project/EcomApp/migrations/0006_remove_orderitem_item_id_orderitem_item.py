# Generated by Django 5.0.3 on 2024-05-08 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomApp', '0005_order_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='item_id',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_items', to='EcomApp.item'),
        ),
    ]