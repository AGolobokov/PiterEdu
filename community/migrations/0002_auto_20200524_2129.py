# Generated by Django 3.0.5 on 2020-05-24 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='status',
        ),
        migrations.AlterField(
            model_name='community',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
