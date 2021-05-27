# Generated by Django 3.2.3 on 2021-05-27 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0024_auto_20210527_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='milage',
            new_name='mileage',
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(default=None, max_length=120),
            preserve_default=False,
        ),
    ]
