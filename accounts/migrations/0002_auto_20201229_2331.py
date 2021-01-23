# Generated by Django 2.2 on 2020-12-29 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trades',
            name='postion',
            field=models.CharField(blank=True, choices=[('Long', 'Long'), ('Short', 'Short')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='trades',
            name='trade_status',
            field=models.CharField(blank=True, choices=[('Running', 'Running'), ('Closed', 'Closed')], max_length=25, null=True),
        ),
    ]
