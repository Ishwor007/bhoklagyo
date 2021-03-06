# Generated by Django 4.0.5 on 2022-07-24 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0002_user_date_joined'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('longitude', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('register_date', models.DateField(auto_now_add=True)),
                ('last_modified_on', models.DateField(auto_now=True)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantAdmin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('restaurant_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to='restaurant_app.restaurant')),
            ],
            options={
                'verbose_name': 'Admin',
                'permissions': (),
            },
            bases=('user_app.user',),
        ),
    ]
