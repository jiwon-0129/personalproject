# Generated by Django 3.2.8 on 2021-11-20 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mad', '0008_restaurant_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='description',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='signature_menu',
            field=models.CharField(default='', max_length=100, verbose_name='Description'),
        ),
    ]
