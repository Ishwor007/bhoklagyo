# Generated by Django 4.0.5 on 2022-10-19 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('restaurant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant', to='restaurant_app.restaurant')),
            ],
            options={
                'verbose_name': 'Admin',
                'db_table': 'Admin',
                'permissions': (),
            },
        ),
    ]
