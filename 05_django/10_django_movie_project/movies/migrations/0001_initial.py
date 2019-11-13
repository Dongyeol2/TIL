# Generated by Django 2.2.6 on 2019-11-01 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200)),
                ('audience', models.IntegerField()),
                ('open_date', models.DateTimeField()),
                ('genre', models.CharField(max_length=200)),
                ('watch_grade', models.CharField(max_length=200)),
                ('score', models.IntegerField()),
                ('poster_url', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
        ),
    ]