# Generated by Django 3.1.2 on 2020-10-27 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='volume',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]