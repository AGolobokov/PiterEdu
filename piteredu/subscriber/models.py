from django.db import models

# Create your models here.


class Subscriber(models.Model):
    name = models.CharField(max_length=128, blank=False,  verbose_name='Имя')  # required to field
    email = models.EmailField(max_length=80, blank=False, verbose_name='Почта')  # required to field
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    def __str__(self):
        return self.name
