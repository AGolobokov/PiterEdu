# Generated by Django 3.0.5 on 2020-05-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_remove_rooms_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
