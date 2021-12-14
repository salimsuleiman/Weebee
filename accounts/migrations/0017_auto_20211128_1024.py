# Generated by Django 3.2.7 on 2021-11-28 10:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_account_accountnumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='date_joined',
            new_name='dateJoined',
        ),
        migrations.RemoveField(
            model_name='accounttype',
            name='maximunWidrawa',
        ),
        migrations.AddField(
            model_name='accounttype',
            name='maximunWidrawal',
            field=models.DecimalField(decimal_places=2, default=12, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='postalCode',
            field=models.PositiveIntegerField(default=1234),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='streetAddress',
            field=models.CharField(default=django.utils.timezone.now, max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='accountNumber',
            field=models.PositiveIntegerField(blank=True, default='006490201830', unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(default=''),
        ),
    ]
