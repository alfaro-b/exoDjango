# Generated by Django 5.1.3 on 2025-04-09 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_slug_alter_article_titre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
