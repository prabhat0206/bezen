# Generated by Django 4.0.2 on 2022-02-17 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bezen', '0002_record_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='length',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='weight',
            field=models.CharField(max_length=50),
        ),
    ]