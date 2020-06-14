from django.db import models

# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # функция для более детально отображения записей в админке
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус публикации"
        verbose_name_plural = "Статусы публикаций"


class StatusPrice(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # функция для более детально отображения записей в админке
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус цены"
        verbose_name_plural = "Статусы цен"
