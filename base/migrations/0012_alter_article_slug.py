# Generated by Django 4.1.3 on 2022-11-28 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=200, unique=True), max_length=200, unique=True),
        ),
    ]
