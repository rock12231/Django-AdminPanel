# Generated by Django 4.0.5 on 2022-07-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datatable', '0003_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
