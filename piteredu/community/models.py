from django.db import models

from status.models import Status
# Create your models here.


class Community(models.Model):
    name = models.CharField(max_length=64, blank=False,  verbose_name='Название')  # required to field
    description = models.TextField(blank=False, verbose_name='Описание')  # required to field
    address = models.CharField(max_length=128, blank=True, verbose_name='Адрес')  # not required to field
    phone = models.CharField(max_length=30, blank=True, verbose_name='Телефон')  # not required to field
    photo = models.ImageField(upload_to="social/social_img",
                              default='', blank=True, verbose_name='Изображение')  # not required to field
    contacts = models.URLField(blank=True, verbose_name='Контакты')  # not required to field
    is_active = models.BooleanField(default=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')  # required to field
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Сообщество'
        verbose_name_plural = 'Сообщества'

    def __str__(self):
        return self.name
