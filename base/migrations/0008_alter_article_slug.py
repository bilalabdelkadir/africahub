# Generated by Django 4.1.3 on 2022-11-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_article_options_article_slug_article_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
