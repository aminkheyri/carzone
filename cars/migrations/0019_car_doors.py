# Generated by Django 3.2.3 on 2021-05-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0018_car_interior'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='doors',
            field=models.IntegerField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default=None),
            preserve_default=False,
        ),
    ]
