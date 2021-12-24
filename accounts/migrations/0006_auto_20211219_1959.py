# Generated by Django 3.2.9 on 2021-12-19 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20211219_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='accountNumber',
            field=models.CharField(blank=True, default=8532148581, max_length=15, unique=True, verbose_name='Account Number'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lastName',
            field=models.CharField(max_length=60, verbose_name='Last Name'),
        ),
    ]
