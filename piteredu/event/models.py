from django.db import models

from status.models import Status, StatusPrice

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=128, blank=False, verbose_name='Название') # required to field
    date = models.DateField(blank=False, verbose_name='Дата') # required to field
    address = models.CharField(max_length=128, blank=True, verbose_name='Адрес')  # not required to field
    link = models.URLField(blank=False, verbose_name='Ссылка на регистрацию') # required to field
    phone = models.CharField(max_length=30, blank=True, verbose_name='Телефон')  # not required to field
    price = models.ForeignKey(StatusPrice, on_delete=models.CASCADE, blank=False, verbose_name='Цена')  # required to field
    description = models.TextField(blank=False, verbose_name='Описание')  # required to field
    photo = models.ImageField(upload_to="event/ivent_img", default='', blank=True, verbose_name='Изображение')  # not required to field
    is_active = models.BooleanField(default=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=False, verbose_name='Статуы')  # required to field

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.name

