# Городская иерархическая структура
"""
Использование до уровня деревни
1. Скачайте данные с помощью https://www.npmjs.com/package/china-division, поместите соответствующий JSON в соответствующий каталог.
2. Измените имя соответствующего JSON в этом файле.
3. Щелкните правой кнопкой мыши и выполните этот файл Python для инициализации.
"""
import json
import os

import django
import pypinyin
from django.core.management import BaseCommand
from django.db import connection

from fuadmin.settings import BASE_DIR
from system.models import Area

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')
django.setup()

area_code_list = []


def area_list(code_list, pcode=None, depth=1):
    """
    Рекурсивно получаем все списки
    """
    for code_dict in code_list:
        code = code_dict.get('code', None)
        name = code_dict.get('name', None)
        children = code_dict.get('children', None)
        pinyin = ''.join([''.join(i) for i in pypinyin.pinyin(name, style=pypinyin.NORMAL)])
        area_code_list.append(
            {
                "name": name,
                "code": code,
                "level": depth,
                "pinyin": pinyin,
                "initials": pinyin[0].upper() if pinyin else "#",
                "pcode_id": pcode,
            }
        )
        if children:
            area_list(code_list=children, pcode=code, depth=depth + 1)


def main():
    with open(os.path.join(BASE_DIR, 'utils', 'pca-code.json'), 'r',encoding="utf-8") as load_f:
        code_list = json.load(load_f)
    area_list(code_list)
    if Area.objects.count() == 0:
        Area.objects.bulk_create([Area(**ele) for ele in area_code_list])
    else:
        for ele in area_code_list:
            code = ele.pop("code")
            Area.objects.update_or_create(code=code, defaults=ele)


class Command(BaseCommand):
    """
    Команда инициализации проекта: python manage.py init
    """

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        print(f"Инициализация данных о регионах...")

        if hasattr(connection, 'tenant') and connection.tenant.schema_name:
            from django_tenants.utils import get_tenant_model
            from django_tenants.utils import tenant_context,schema_context
            for tenant in get_tenant_model().objects.exclude(schema_name='public'):
                with tenant_context(tenant):
                    print(f"Инициализация данных для арендатора [{connection.tenant.schema_name}]...")
                    main()
                    print(f"Инициализация данных для арендатора [{connection.tenant.schema_name}] завершена!")
        else:
            main()
        print("Инициализация данных о регионах завершена!")