# Generated by Django 5.0.3 on 2024-03-11 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='date_new',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
