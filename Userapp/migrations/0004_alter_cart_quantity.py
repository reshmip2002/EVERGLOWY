# Generated by Django 4.2.10 on 2024-03-03 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0003_alter_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.CharField(default='1', max_length=20, null=True),
        ),
    ]