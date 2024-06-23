from django.db import models
from utils.models import CoreModel


class Demo(CoreModel):
    name = models.CharField(null=False, max_length=64, verbose_name="Название проекта", help_text="Название проекта")
    code = models.CharField(max_length=32, verbose_name="Код проекта", help_text="Код проекта")
    status = models.CharField(max_length=64, verbose_name="Статус проекта", help_text="Статус проекта")

    class Meta:
        db_table = "Demo"
        verbose_name = 'Демонстрация проекта'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)