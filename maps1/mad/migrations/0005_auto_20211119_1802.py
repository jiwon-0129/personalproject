# Generated by Django 3.2.8 on 2021-11-19 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mad', '0004_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='family',
            field=models.BooleanField(default='True'),
        ),
        migrations.AlterField(
            model_name='filter',
            name='friends',
            field=models.BooleanField(default='True'),
        ),
        migrations.AlterField(
            model_name='filter',
            name='lovers',
            field=models.BooleanField(default='True'),
        ),
        migrations.AlterField(
            model_name='filter',
            name='self',
            field=models.BooleanField(default='True'),
        ),
        migrations.AlterField(
            model_name='filter',
            name='senior',
            field=models.BooleanField(default='True'),
        ),
    ]
