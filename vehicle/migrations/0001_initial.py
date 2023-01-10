# Generated by Django 3.1.7 on 2021-04-24 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=250)),
                ('vehicle_type', models.TextField(max_length=100)),
                ('color', models.TextField(max_length=50)),
                ('license_plate_no', models.TextField(max_length=250)),
            ],
        ),
    ]
