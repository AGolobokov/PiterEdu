# Generated by Django 3.0.5 on 2020-05-09 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('date', models.DateField(verbose_name='Дата')),
                ('address', models.CharField(blank=True, max_length=128, verbose_name='Адрес')),
                ('link', models.URLField(verbose_name='Ссылка на регистрацию')),
                ('phone', models.CharField(blank=True, max_length=30, verbose_name='Телефон')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, default='', upload_to='event/ivent_img', verbose_name='Изображение')),
                ('is_active', models.BooleanField(default=True)),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.StatusPrice', verbose_name='Цена')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.Status', verbose_name='Статуы')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
    ]
