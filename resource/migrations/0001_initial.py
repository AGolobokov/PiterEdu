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
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, default='', upload_to='resource/resource_img', verbose_name='Изображение')),
                ('contacts', models.URLField(blank=True, verbose_name='Контакты')),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.Status', verbose_name='Статуы')),
            ],
            options={
                'verbose_name': 'Ресурс',
                'verbose_name_plural': 'Ресурсы',
            },
        ),
    ]