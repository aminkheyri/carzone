# Generated by Django 3.2.3 on 2021-05-27 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0017_car_transmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='interior',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
