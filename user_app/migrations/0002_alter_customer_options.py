# Generated by Django 4.0.5 on 2022-07-01 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
    ]