# Generated by Django 2.2 on 2020-12-29 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201229_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trades',
            name='profit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=1000000, null=True, verbose_name='Profit'),
        ),
    ]