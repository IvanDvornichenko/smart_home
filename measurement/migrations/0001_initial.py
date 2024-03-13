# Generated by Django 5.0.3 on 2024-03-11 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_new', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('temperature', models.FloatField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor')),
            ],
        ),
    ]
