# Generated by Django 3.2.7 on 2021-11-28 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20211128_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='accountNumber',
            field=models.CharField(blank=True, default='007291485866', max_length=15),
        ),
    ]