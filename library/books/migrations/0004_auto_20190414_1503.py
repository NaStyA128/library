# Generated by Django 2.2 on 2019-04-14 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190414_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.DateField(blank=True),
        ),
    ]
