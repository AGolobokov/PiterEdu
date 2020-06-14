from django.db import models

from status.models import Status
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=128, blank=False, verbose_name='Название')  # required to field
    description = models.TextField(blank=False, verbose_name='Описание')  # required to field
    # photo = models.ImageField(upload_to="resource/resource_img", default='', blank=True,
    #                       verbose_name='Изображение')  # not required to field
    link = models.URLField(blank=True, verbose_name='Сайт')  # not required to field
    is_active = models.BooleanField(default=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=False,
                               verbose_name='Статуы')  # required to field

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='project/project_img', default='', blank=True,
                            verbose_name='Изображение')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

# функция для более детально отображения записей в админке
    def __str__(self):
        return "%s" % self.id
#
#     def __str__(self):
#         return self.id

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


