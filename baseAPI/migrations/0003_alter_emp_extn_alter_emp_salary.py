# Generated by Django 4.0.5 on 2022-07-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseAPI', '0002_emp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='extn',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AlterField(
            model_name='emp',
            name='salary',
            field=models.IntegerField(blank=True, default='0'),
        ),
    ]