# Generated by Django 3.2.8 on 2021-11-19 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mad', '0003_auto_20211119_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.BooleanField(default='')),
                ('friends', models.BooleanField(default='')),
                ('self', models.BooleanField(default='')),
                ('lovers', models.BooleanField(default='')),
                ('senior', models.BooleanField(default='')),
            ],
        ),
    ]
