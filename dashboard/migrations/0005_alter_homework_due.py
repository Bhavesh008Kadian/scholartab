# Generated by Django 4.0.6 on 2022-08-07 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='due',
            field=models.DateField(),
        ),
    ]
