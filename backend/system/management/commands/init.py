import logging

from django.core.management.base import BaseCommand

from fuadmin import settings

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    Команда инициализации проекта: python manage.py init
    """

    def add_arguments(self, parser):
        parser.add_argument('init_name', nargs='*', type=str, )
        parser.add_argument('-y', nargs='*')
        parser.add_argument('-Y', nargs='*')
        parser.add_argument('-n', nargs='*')
        parser.add_argument('-N', nargs='*')

    def handle(self, *args, **options):
        reset = False
        if isinstance(options.get('y'), list) or isinstance(options.get('Y'), list):
            reset = True
        if isinstance(options.get('n'), list) or isinstance(options.get('N'), list):
            reset = False
        print(f"Подготовка к инициализации данных. {'Если данные уже инициализированы, они будут пропущены.' if not reset else 'Существующие данные будут удалены перед добавлением новых.'}...")

        for app in settings.INSTALLED_APPS:

            try:
                exec(f"""
from {app}.initialize import main
main(reset={reset})
                """)
            except ModuleNotFoundError:
                pass
        print("Инициализация данных завершена!")