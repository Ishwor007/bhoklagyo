# Generated by Django 4.0.5 on 2022-07-13 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_alter_user_options_remove_user_date_joined_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='staff',
        ),
    ]