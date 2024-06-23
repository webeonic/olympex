import json
import logging
import os
import shutil

from django.core.management.base import BaseCommand

from fuadmin.settings import BASE_DIR

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Команда для создания приложения:
    python manage.py createapp имя_приложения
    python manage.py createapp приложение01 приложение02 ...
    python manage.py createapp имя_файла_верхнего_уровня/приложение01 ...    # Поддерживает создание приложений в многоуровневых каталогах
    """

    def add_arguments(self, parser):
        parser.add_argument('app_info', nargs='*', type=str, )

    def handle(self, *args, **options):
        app_info = options.get('app_info')
        for name in app_info:
            app = json.loads(name)
            name = app.get('app_name')
            names = name.split('/')
            dnames = ".".join(names)
            app_path = os.path.join(BASE_DIR, "dvadmin", *names)
            # Проверить, существует ли приложение
            if os.path.exists(app_path):
                print(f"Приложение {name} уже существует!")
                # break
            else:
                source_path = os.path.join(BASE_DIR, "dvadmin", "utils", "template")
                target_path = app_path
                if not os.path.exists(target_path):
                    # Если целевой путь не содержит исходную папку, создать ее
                    os.makedirs(target_path)
                if os.path.exists(source_path):
                    # Если целевой путь содержит исходную папку, сначала удалить ее
                    shutil.rmtree(target_path)
                shutil.copytree(source_path, target_path)
                # Зарегистрировать приложение в settings.py
                injection(os.path.join(BASE_DIR, "application", "settings.py"), f"    'dvadmin.{dnames}',\n",
                          "INSTALLED_APPS",
                          "]")

                # Зарегистрировать приложение в urls.py
                injection(os.path.join(BASE_DIR, "application", "urls.py"),
                          f"    path(r'api/{name}/', include('dvadmin.{dnames}.urls')),\n", "urlpatterns = [",
                          "]")

            # Изменить содержимое apps в приложении
            app_content = f"""
from django.apps import AppConfig


class {name.capitalize()}Config(AppConfig):
    name = 'dvadmin.{dnames}'
    verbose_name = "{names[-1]}App"
"""
            with open(os.path.join(app_path, "apps.py"), 'w', encoding='UTF-8') as f:
                f.write(app_content)

            # Изменить содержимое Model
            table_name = app.get('table_name')
            model_name = app.get('model_name')

            # Все не повторяющиеся поля в приложении
            app_fields = app.get('fields')
            field_content = ''
            # Все не повторяющиеся типы полей в приложении
            fields_type = set()
            # Все имена полей в приложении
            fields_name = set()
            for field in app_fields:
                fields_type.add(field['type'])
                fields_name.add(field['name'])
                if field['type'] == 'CharField':
                    field_content = f"""{field_content}
    {field['name']} = {field['type']}(max_length={field['max_length']}, verbose_name='{field['name']}', help_text='{field['description']}')"""
                elif field['type'] == 'TextField':
                    field_content = f"""{field_content}
    {field['name']} = {field['type']}(verbose_name='{field['name']}', help_text='{field['description']}')"""
            model_content = f"""
from django.db.models import {','.join(fields_type)}
from dvadmin.utils.models import CoreModel


class {model_name}(CoreModel):
{field_content}

    class Meta:
        verbose_name = '{model_name}'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.{fields_name.pop()} 
"""

            with open(os.path.join(app_path, "models", f"{table_name}.py"), 'w', encoding='UTF-8') as f:
                f.write(model_content)

            # Изменить файл init модели
            model_init_content = f"from dvadmin.{name}.models.{table_name} import {model_name}"
            with open(os.path.join(app_path, "models", "__init__.py"), 'a', encoding='UTF-8') as f:
                f.write(model_init_content)
                f.write('\n')

            # Изменить содержимое filters
            filter_content = f"""
import django_filters
from dvadmin.{name}.models import {model_name}


class {model_name}Filter(django_filters.rest_framework.FilterSet):

    # С помощью lookup_expr можно выполнять нечеткий поиск, другие конфигурации можно найти самостоятельно в Google
    # name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = {model_name}
        fields = '__all__'

"""
            with open(os.path.join(app_path, "filters", f"{table_name}_filter.py"), 'w', encoding='UTF-8') as f:
                f.write(filter_content)

            # Изменить файл init filters
            filter_init_content = f"from .{table_name}_filter import {model_name}Filter"
            with open(os.path.join(app_path, "filters", "__init__.py"), 'a', encoding='UTF-8') as f:
                f.write(filter_init_content)
                f.write('\n')

            # Изменить содержимое serializers
            serializer_content = f"""
from rest_framework import serializers
from dvadmin.{name}.models import {model_name}
from dvadmin.utils.serializers import CustomModelSerializer


class {model_name}Serializer(CustomModelSerializer):

    class Meta:
        model = {model_name}
        fields = '__all__'
        
        
class {model_name}CreateUpdateSerializer(CustomModelSerializer):

    # Здесь можно написать настраиваемое создание/обновление
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = {model_name}
        fields = '__all__'


class {model_name}ImportSerializer(CustomModelSerializer):

    class Meta:
        model = {model_name}
        fields = '__all__'


class {model_name}ExportSerializer(CustomModelSerializer):

    class Meta:
        model = {model_name}
        fields = '__all__'

"""
            with open(os.path.join(app_path, 'serializers', f'{table_name}_serializer.py'), 'w', encoding='UTF-8') as f:
                f.write(serializer_content)

            # Изменить файл init serializers
            serializer_init_content = f"from .{table_name}_serializer import {model_name}Serializer, " \
                                      f"{model_name}CreateUpdateSerializer, " \
                                      f"{model_name}ImportSerializer, " \
                                      f"{model_name}ExportSerializer"
            with open(os.path.join(app_path, "serializers", "__init__.py"), 'a', encoding='UTF-8') as f:
                f.write(serializer_init_content)
                f.write('\n')
            # Изменить содержимое view
            view_content = f"""
from dvadmin.utils.filters import DataLevelPermissionsFilter
from dvadmin.utils.viewset import CustomModelViewSet
from dvadmin.{name}.models import {model_name}
from dvadmin.{name}.filters import {model_name}Filter
from dvadmin.{name}.serializers import {model_name}Serializer, {model_name}CreateUpdateSerializer, {model_name}ImportSerializer, {model_name}ExportSerializer
                            
          
class {model_name}ModelViewSet(CustomModelViewSet):

    queryset = {model_name}.objects.all()
    serializer_class = {model_name}Serializer  # Сериализатор
    create_serializer_class = {model_name}CreateUpdateSerializer  # Сериализатор при создании/обновлении
    update_serializer_class = {model_name}CreateUpdateSerializer  # Сериализатор при создании/обновлении
    filter_class = {model_name}Filter  # Фильтр
    extra_filter_backends = [DataLevelPermissionsFilter]  # Класс прав доступа к данным, можно закомментировать, если он не нужен
    # ordering = ['create_datetime']  # Сортировка по умолчанию
    # Экспорт
    export_field_data = []  # Экспорт
    export_serializer_class = {model_name}ExportSerializer  # Сериализатор для экспорта
    # Импорт
    import_field_data = []
    import_serializer_class = {model_name}ImportSerializer


"""
            with open(os.path.join(app_path, 'views', f'{table_name}_view.py'), 'w', encoding='UTF-8') as f:
                f.write(view_content)

            # Изменить файл init views
            view_init_content = f"from .{table_name}_view import {model_name}ModelViewSet"
            with open(os.path.join(app_path, "views", "__init__.py"), 'a', encoding='UTF-8') as f:
                f.write(view_init_content)
                f.write('\n')

            # Изменить файл url
            url_package = f"from dvadmin.{name}.views import {model_name}ModelViewSet"
            injection(os.path.join(app_path, "urls.py"),
                      f"{url_package}\n", "from rest_framework.routers import DefaultRouter",
                      "router = DefaultRouter()")

            url_path = f"router.register(r'{table_name}', {model_name}ModelViewSet)"
            injection(os.path.join(app_path, "urls.py"),
                      f"{url_path}\n", "router = DefaultRouter()",
                      "urlpatterns = [")

            export_import_url = f"""    # Экспорт проекта
    path('{table_name}/export/', {model_name}ModelViewSet.as_view({{'get': 'export', }})),
    # Шаблон импорта проекта для скачивания и импорта
    path('{table_name}/importTemplate/', {model_name}ModelViewSet.as_view({{'get': 'importTemplate', 'post': 'importTemplate'}}))"""
            injection(os.path.join(app_path, "urls.py"),
                      f"{export_import_url}\n", "urlpatterns = [", "]")

            print(f"Приложение {name} создано успешно")


def injection(file_path, insert_content, startswith, endswith):
    with open(file_path, "r+", encoding="utf-8") as f:
        data = f.readlines()
        with open(file_path, 'w', encoding='UTF-8') as f1:
            is_INSTALLED_APPS = False
            is_insert = False
            for content in data:
                # Проверить, начинается ли файл с INSTALLED_APPS
                if not is_insert and content.startswith(startswith):
                    is_INSTALLED_APPS = True
                if not is_insert and content.startswith(endswith) and is_INSTALLED_APPS:
                    # Вставить данные в предыдущую строку
                    content = insert_content + content
                    is_insert = True
                f1.writelines(content)