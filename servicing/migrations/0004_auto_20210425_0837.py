# Generated by Django 3.1.7 on 2021-04-25 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicing', '0003_auto_20210425_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicing',
            name='pick_up_date',
            field=models.TextField(),
        ),
    ]
