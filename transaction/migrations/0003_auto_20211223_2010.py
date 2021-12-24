# Generated by Django 3.2.9 on 2021-12-23 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_auto_20211223_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transtype',
            field=models.IntegerField(choices=[(0, 'Debit'), (1, 'Credit')], null=True, verbose_name='Transaction Type'),
        ),
    ]
