# Generated by Django 3.0.8 on 2020-07-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='Jonathan Axelsson', max_length=100),
            preserve_default=False,
        ),
    ]