# Generated by Django 3.2.7 on 2021-11-27 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
