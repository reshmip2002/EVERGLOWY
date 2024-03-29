# Generated by Django 4.2.10 on 2024-02-19 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Sellerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'Admin_table',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'event_table',
            },
        ),
        migrations.CreateModel(
            name='LocationState',
            fields=[
                ('state_id', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'state_table',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('offer_id', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('discount', models.CharField(max_length=20, null=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminapp.event')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sellerapp.product')),
            ],
            options={
                'db_table': 'offer_table',
            },
        ),
        migrations.CreateModel(
            name='LocationDistrict',
            fields=[
                ('district_id', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('district_name', models.CharField(max_length=50, null=True)),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminapp.locationstate')),
            ],
            options={
                'db_table': 'district_table',
            },
        ),
        migrations.CreateModel(
            name='LocationCity',
            fields=[
                ('city_id', models.IntegerField(default=None, primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=50, null=True)),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminapp.locationdistrict')),
            ],
            options={
                'db_table': 'city_table',
            },
        ),
    ]
