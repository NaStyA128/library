# Generated by Django 2.2 on 2019-04-14 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190414_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='additional_information',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='biography',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='additional_information',
            field=models.TextField(blank=True),
        ),
    ]
