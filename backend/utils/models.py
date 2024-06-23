# -*- coding: utf-8 -*-

"""
@author: 猿小天
@contact: QQ:1638245306
@Created on: 2021/5/31 031 22:08
@Remark: 公共基础model类
"""
import uuid

from django.apps import apps
from django.db import models

from fuadmin import settings


class CoreModel(models.Model):
    """
    Базовая абстрактная модель, которая может быть унаследована.
    Добавляет поля аудита. При переопределении имен полей не изменяйте их. Имена полей аудита должны быть едиными.
    """
    id = models.BigAutoField(primary_key=True, help_text="Идентификатор", verbose_name="Идентификатор")
    remark = models.CharField(max_length=255, verbose_name="Описание", null=True, blank=True, help_text="Описание")
    creator = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_query_name='creator_query', null=True,
                                verbose_name='Создатель', help_text="Создатель", on_delete=models.SET_NULL, db_constraint=False)
    modifier = models.CharField(max_length=255, null=True, blank=True, help_text="Модификатор", verbose_name="Модификатор")
    belong_dept = models.IntegerField(help_text="Отдел, которому принадлежат данные", null=True, blank=True, verbose_name="Отдел, которому принадлежат данные")
    update_datetime = models.DateTimeField(auto_now=True, null=True, blank=True, help_text="Дата обновления", verbose_name="Дата обновления")
    create_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True, help_text="Дата создания",
                                           verbose_name="Дата создания")
    sort = models.IntegerField(default=1, null=True, blank=True, verbose_name="Порядок сортировки отображения", help_text="Порядок сортировки отображения")

    class Meta:
        abstract = True
        verbose_name = 'Базовая модель'
        verbose_name_plural = verbose_name


def get_all_models_objects(model_name=None):
    """
    Получить все объекты моделей
    :return: {}
    """
    settings.ALL_MODELS_OBJECTS = {}
    if not settings.ALL_MODELS_OBJECTS:
        all_models = apps.get_models()
        for item in list(all_models):
            table = {
                "tableName": item._meta.verbose_name,
                "table": item.__name__,
                "tableFields": []
            }
            for field in item._meta.fields:
                fields = {
                    "title": field.verbose_name,
                    "field": field.name
                }
                table['tableFields'].append(fields)
            settings.ALL_MODELS_OBJECTS.setdefault(item.__name__, {"table": table, "object": item})
    if model_name:
        return settings.ALL_MODELS_OBJECTS[model_name] or {}
    return settings.ALL_MODELS_OBJECTS or {}