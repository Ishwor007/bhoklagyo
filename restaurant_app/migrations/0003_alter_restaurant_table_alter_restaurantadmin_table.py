# Generated by Django 4.0.5 on 2022-10-21 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='restaurant',
            table='restaurant',
        ),
        migrations.AlterModelTable(
            name='restaurantadmin',
            table='restaurant_admin',
        ),
    ]
