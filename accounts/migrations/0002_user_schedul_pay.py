# Generated by Django 2.2 on 2021-02-14 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='schedul_pay',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Scheduled payment'),
        ),
    ]