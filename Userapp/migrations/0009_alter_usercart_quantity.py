# Generated by Django 4.2.10 on 2024-03-03 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0008_alter_usercart_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
