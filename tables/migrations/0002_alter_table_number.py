# Generated by Django 4.0.1 on 2022-01-21 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]