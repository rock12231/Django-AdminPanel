# Generated by Django 4.0.5 on 2022-07-09 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseAPI', '0004_alter_emp_salary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emp',
            options={'ordering': ['start_date']},
        ),
    ]
