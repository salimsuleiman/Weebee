# Generated by Django 3.2.7 on 2021-11-27 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='weebeeAddress',
            field=models.CharField(max_length=200, null=True),
        ),
    ]