# Generated by Django 4.0.5 on 2022-07-12 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customer',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterModelTable(
            name='customer',
            table='Customer',
        ),
    ]