# Generated by Django 2.2 on 2020-12-29 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201229_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trades',
            name='lot_size',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=100, null=True, verbose_name='Lot size'),
        ),
    ]