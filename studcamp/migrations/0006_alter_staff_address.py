# Generated by Django 3.2.16 on 2022-11-03 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studcamp', '0005_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='address',
            field=models.CharField(max_length=550),
        ),
    ]
