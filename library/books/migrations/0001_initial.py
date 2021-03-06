# Generated by Django 2.2 on 2019-04-10 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_slug', models.CharField(max_length=50)),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('text', models.TextField()),
                ('year', models.PositiveIntegerField(blank=True, null=True)),
                ('author', models.ManyToManyField(null=True, to='users.Author')),
                ('genre', models.ManyToManyField(null=True, to='books.Genre')),
            ],
        ),
    ]
