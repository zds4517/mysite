# Generated by Django 2.1.7 on 2020-11-29 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201129_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='readed_num',
            field=models.IntegerField(default=0, verbose_name='阅读数'),
        ),
    ]