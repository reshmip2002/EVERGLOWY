# Generated by Django 4.2.10 on 2024-03-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0009_alter_usercart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='list_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
