from django.db import models

from status.models import Status
# Create your models here.


class Resource(models.Model):
    name = models.CharField(max_length=128, blank=False,  verbose_name='Название')  # required to field
    description = models.TextField(blank=False, verbose_name='Описание')  # required to field
    photo = models.ImageField(upload_to="resource/resource_img", default='', blank=True,
                              verbose_name='Изображение')  # not required to field
    contacts = models.URLField(blank=True, verbose_name='Контакты')  # not required to field
    is_active = models.BooleanField(default=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=False,
                               verbose_name='Статуы')  # required to field

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'

    def __str__(self):
        return self.name

