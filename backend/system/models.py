import hashlib
import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.models import CoreModel

STATUS_CHOICES = (
    (0, "Запретить"),
    (1, "Использовать"),
)


class Users(AbstractUser, CoreModel):
    username = models.CharField(max_length=150, unique=True, db_index=True, verbose_name='Учетная запись пользователя',
                                help_text="Учетная запись пользователя")
    email = models.EmailField(max_length=255, verbose_name="Электронная почта", null=True, blank=True, help_text="Электронная почта")
    mobile = models.CharField(max_length=255, verbose_name="Телефон", null=True, blank=True, help_text="Телефон")
    avatar = models.TextField(verbose_name="Аватар", null=True, blank=True, help_text="Аватар")
    name = models.CharField(max_length=40, verbose_name="Имя", help_text="Имя")
    status = models.BooleanField(default=True, verbose_name="Состояние", help_text="Состояние")
    GENDER_CHOICES = (
        (0, "Женский"),
        (1, "Мужской"),
    )
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1, verbose_name="Пол", null=True, blank=True,
                                 help_text="Пол")
    USER_TYPE = (
        (0, "Пользователь бэкэнда"),
        (1, "Пользователь фронтэнда"),
    )
    user_type = models.IntegerField(choices=USER_TYPE, default=0, verbose_name="Тип пользователя", null=True, blank=True,
                                    help_text="Тип пользователя")
    post = models.ManyToManyField(to='Post', verbose_name='Связанные должности', db_constraint=False, help_text="Связанные должности")
    role = models.ManyToManyField(to='Role', verbose_name='Связанные роли', db_constraint=False, help_text="Связанные роли")
    dept = models.ForeignKey(to='Dept', verbose_name='Отдел, которому принадлежит пользователь', on_delete=models.SET_NULL, db_constraint=False,
                             null=True,
                             blank=True, help_text="Связанный отдел")
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    home_path = models.CharField(max_length=150, blank=True, null=True)


    class Meta:
        db_table = "system_users"
        verbose_name = 'Таблица пользователей'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)


class Post(CoreModel):
    name = models.CharField(null=False, max_length=64, verbose_name="Название должности", help_text="Название должности")
    code = models.CharField(max_length=32, verbose_name="Код должности", help_text="Код должности")
    STATUS_CHOICES = (
        (0, "Уволен"),
        (1, "Работает"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="Состояние должности", help_text="Состояние должности")

    class Meta:
        db_table = "system_post"
        verbose_name = 'Таблица должностей'
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class Role(CoreModel):
    name = models.CharField(max_length=64, verbose_name="Название роли", help_text="Название роли")
    code = models.CharField(max_length=64, unique=True, verbose_name="Код роли", help_text="Код роли")
    # key = models.CharField(max_length=64, unique=True, verbose_name="权限字符", help_text="权限字符")
    status = models.BooleanField(default=True, verbose_name="Состояние роли", help_text="Состояние роли")
    admin = models.BooleanField(default=False, verbose_name="Является ли администратором", help_text="Является ли администратором")
    DATASCOPE_CHOICES = (
        (0, "Только данные для себя"),
        (1, "Данные отдела"),
        (2, "Данные отдела и его подчиненных"),
        (3, "Все данные"),
        (4, "Пользовательские данные"),
    )
    data_range = models.IntegerField(default=0, choices=DATASCOPE_CHOICES, verbose_name="Диапазон полномочий доступа к данным",
                                     help_text="Диапазон полномочий доступа к данным")
    dept = models.ManyToManyField(to='Dept', verbose_name='Разрешения на данные - связанный отдел', db_constraint=False,
                                  help_text="Разрешения на данные - связанный отдел")
    menu = models.ManyToManyField(to='Menu', verbose_name='Связанное меню', db_constraint=False, help_text="Связанное меню")
    permission = models.ManyToManyField(to='MenuButton', verbose_name='Связанные кнопки интерфейса меню', db_constraint=False,
                                        help_text="Связанные кнопки интерфейса меню")
    column = models.ManyToManyField(to='MenuColumnField', verbose_name='Разрешения на списки', db_constraint=False,
                                    help_text="Разрешения на списки")

    class Meta:
        db_table = 'system_role'
        verbose_name = 'Таблица ролей'
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class Dept(CoreModel):
    name = models.CharField(max_length=64, verbose_name="Название отдела", help_text="Название отдела")
    owner = models.CharField(max_length=32, verbose_name="Ответственный", null=True, blank=True, help_text="Ответственный")
    phone = models.CharField(max_length=32, verbose_name="Контактный телефон", null=True, blank=True, help_text="Контактный телефон")
    email = models.EmailField(max_length=32, verbose_name="Электронная почта", null=True, blank=True, help_text="Электронная почта")
    status = models.BooleanField(default=True, verbose_name="Состояние отдела", null=True, blank=True,
                                 help_text="Состояние отдела")
    parent = models.ForeignKey(to='Dept', on_delete=models.PROTECT, default=None, verbose_name="Родительский отдел",
                               db_constraint=False, null=True, blank=True, help_text="Родительский отдел")

    class Meta:
        db_table = "system_dept"
        verbose_name = 'Таблица отделов'
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class Button(CoreModel):
    name = models.CharField(max_length=64, unique=True, verbose_name="Название разрешения", help_text="Название разрешения")
    code = models.CharField(max_length=64, unique=True, verbose_name="Значение разрешения", help_text="Значение разрешения")
    status = models.BooleanField(default=True, verbose_name="Состояние кнопки", null=True, blank=True, help_text="Состояние кнопки")

    class Meta:
        db_table = "system_button"
        verbose_name = 'Таблица разрешений'
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class Menu(CoreModel):
    parent = models.ForeignKey(to='Menu', on_delete=models.CASCADE, verbose_name="Родительское меню", null=True, blank=True,
                               db_constraint=False, help_text="Родительское меню")
    icon = models.CharField(max_length=64, default='ant-design:book-outlined', verbose_name="Иконка меню",
                            help_text="Иконка меню")
    title = models.CharField(max_length=64, verbose_name="Название меню", help_text="Название меню")
    permission = models.CharField(max_length=64, null=True, blank=True, verbose_name="Идентификатор разрешения", help_text="Идентификатор разрешения")
    ISLINK_CHOICES = (
        (0, "Нет"),
        (1, "Да"),
    )
    is_ext = models.BooleanField(default=False, verbose_name="Внешняя ссылка", help_text="Внешняя ссылка")

    TYPE_CHOICES = (
        (0, "Каталог"),
        (1, "Меню"),
    )
    type = models.IntegerField(choices=TYPE_CHOICES, verbose_name="Каталог", help_text="Каталог")
    path = models.CharField(max_length=128, verbose_name="Адрес маршрута", null=True, blank=True, help_text="Адрес маршрута")
    redirect = models.CharField(max_length=128, verbose_name="Адрес перенаправления", null=True, blank=True,
                                help_text="Адрес перенаправления")

    component = models.CharField(max_length=128, verbose_name="Адрес компонента", null=True, blank=True, help_text="Адрес компонента")
    name = models.CharField(max_length=50, verbose_name="Название компонента", null=True, blank=True, help_text="Название компонента")
    status = models.BooleanField(default=True, blank=True, verbose_name="Состояние меню", help_text="Состояние меню")
    keepalive = models.BooleanField(default=False, blank=True, verbose_name="Кэширование страницы", help_text="Кэширование страницы")
    hide_menu = models.BooleanField(default=False, blank=True, verbose_name="Скрыть в боковой панели",
                                    help_text="Скрыть в боковой панели")

    class Meta:
        db_table = "system_menu"
        verbose_name = 'Таблица меню'
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class MenuButton(CoreModel):
    menu = models.ForeignKey(to="Menu", db_constraint=False, related_name="menuPermission", on_delete=models.CASCADE,
                             verbose_name="Связанное меню", help_text='Связанное меню')
    name = models.CharField(max_length=64, verbose_name="Название", help_text="Название")
    code = models.CharField(max_length=64, verbose_name="Значение разрешения", help_text="Значение разрешения")
    api = models.CharField(max_length=200, verbose_name="Адрес интерфейса", help_text="Адрес интерфейса")
    METHOD_CHOICES = (
        (0, "GET"),
        (1, "POST"),
        (2, "PUT"),
        (3, "DELETE"),
    )
    method = models.IntegerField(default=0, verbose_name="Метод запроса интерфейса", null=True, blank=True,
                                 help_text="Метод запроса интерфейса")

    class Meta:
        db_table = "system_menu_button"
        verbose_name = 'Таблица разрешений меню'
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class MenuColumnField(CoreModel):
    menu = models.ForeignKey(to="Menu", db_constraint=False, related_name="menuColumnField", on_delete=models.CASCADE,
                             verbose_name="Связанное меню", help_text='Связанное меню')
    name = models.CharField(max_length=64, verbose_name="Название", help_text="Название")
    code = models.CharField(max_length=64, verbose_name="Значение разрешения", help_text="Значение разрешения")

    class Meta:
        db_table = "system_menu_column_field"
        verbose_name = 'Список данных меню'
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class Dict(CoreModel):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Название словаря", help_text="Название словаря")
    code = models.CharField(max_length=100, blank=True, null=True, verbose_name="Кодировка", help_text="Кодировка")
    status = models.BooleanField(default=True, blank=True, verbose_name="Состояние", help_text="Состояние")
    remark = models.CharField(max_length=2000, blank=True, null=True, verbose_name="Заметка", help_text="Заметка")

    class Meta:
        db_table = 'system_dict'
        verbose_name = "Таблица словарей"
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class DictItem(CoreModel):
    icon = models.CharField(max_length=100, blank=True, null=True, verbose_name="ICON", help_text="ICON")
    label = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отображаемое имя", help_text="Отображаемое имя")
    value = models.CharField(max_length=100, blank=True, null=True, verbose_name="Фактическое значение", help_text="Фактическое значение")
    status = models.BooleanField(default=True, blank=True, verbose_name="Состояние", help_text="Состояние")
    dict = models.ForeignKey(to="Dict", db_constraint=False, related_name="dictItem", on_delete=models.CASCADE,
                             help_text="Словарь")
    remark = models.CharField(max_length=2000, blank=True, null=True, verbose_name="Заметка", help_text="Заметка")

    class Meta:
        db_table = 'system_dict_item'
        verbose_name = "Таблица подробностей словаря"
        verbose_name_plural = verbose_name
        ordering = ('sort',)

class CategoryDict(CoreModel):
    label = models.CharField(max_length=100, blank=True, null=True, verbose_name="Отображаемое имя", help_text="Отображаемое имя")
    value = models.CharField(max_length=100, blank=True, null=True, verbose_name="Фактическое значение", help_text="Фактическое значение")
    code = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name="Кодировка", help_text="Кодировка")
    parent = models.ForeignKey(to='CategoryDict', on_delete=models.CASCADE, default=None, verbose_name="Родительский элемент",
                               db_constraint=False, null=True, blank=True, help_text="Родительский элемент")

    class Meta:
        db_table = 'system_category_dict'
        verbose_name = "Таблица категорий словаря"
        verbose_name_plural = verbose_name
        ordering = ('sort',)


class OperationLog(CoreModel):
    request_username = models.CharField(max_length=50, blank=True, null=True, verbose_name="Запрашивающий пользователь",
                                        help_text="Запрашивающий пользователь")
    request_modular = models.CharField(max_length=64, verbose_name="Запрашиваемый модуль", null=True, blank=True,
                                       help_text="Запрашиваемый модуль")
    request_path = models.CharField(max_length=400, verbose_name="Запрашиваемый адрес", null=True, blank=True,
                                    help_text="Запрашиваемый адрес")
    request_body = models.TextField(verbose_name="Запрашиваемые параметры", null=True, blank=True, help_text="Запрашиваемые параметры")
    request_method = models.CharField(max_length=8, verbose_name="Метод запроса", null=True, blank=True,
                                      help_text="Метод запроса")
    request_msg = models.TextField(verbose_name="Пояснение к операции", null=True, blank=True, help_text="Пояснение к операции")
    request_ip = models.CharField(max_length=32, verbose_name="Запрашиваемый IP-адрес", null=True, blank=True,
                                  help_text="Запрашиваемый IP-адрес")
    request_browser = models.CharField(max_length=64, verbose_name="Запрашиваемый браузер", null=True, blank=True,
                                       help_text="Запрашиваемый браузер")
    response_code = models.CharField(max_length=32, verbose_name="Код состояния ответа", null=True, blank=True,
                                     help_text="Код состояния ответа")
    request_os = models.CharField(max_length=64, verbose_name="Операционная система", null=True, blank=True, help_text="Операционная система")
    json_result = models.TextField(verbose_name="Возвращаемая информация", null=True, blank=True, help_text="Возвращаемая информация")
    status = models.BooleanField(default=False, verbose_name="Состояние ответа", help_text="Состояние ответа")

    class Meta:
        db_table = 'system_operation_log'
        verbose_name = 'Журнал операций'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)


def media_file_name(instance, filename):
    h = instance.md5sum
    basename, ext = os.path.splitext(filename)
    return os.path.join('files', h[0:1], h[1:2], h + ext.lower())


class File(CoreModel):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Фактическое имя", help_text="Фактическое имя")
    save_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Сохраненное имя", help_text="Сохраненное имя")
    url = models.FileField(upload_to=media_file_name)
    size = models.BigIntegerField(null=True, blank=True, verbose_name="Размер", help_text="Размер")
    md5sum = models.CharField(max_length=36, blank=True, verbose_name="MD5-сумма файла", help_text="MD5-сумма файла")

    class Meta:
        db_table = 'system_file'
        verbose_name = 'Управление файлами'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)


class Area(CoreModel):
    name = models.CharField(max_length=100, verbose_name="Название", help_text="Название")
    code = models.CharField(max_length=20, verbose_name="Код региона", help_text="Код региона", unique=True, db_index=True)
    level = models.BigIntegerField(verbose_name="Уровень региона (1 – область, 2 – город, 3 – район, 4 – поселение)",
                                   help_text="Уровень региона (1 – область, 2 – город, 3 – район, 4 – поселение)")
    pinyin = models.CharField(max_length=255, verbose_name="Пиньинь", help_text="Пиньинь")
    initials = models.CharField(max_length=20, verbose_name="Первая буква", help_text="Первая буква")
    enable = models.BooleanField(default=True, verbose_name="Включен", help_text="Включен")
    pcode = models.ForeignKey(to='self', verbose_name='Код родительского региона', to_field="code", on_delete=models.CASCADE,
                              db_constraint=False, null=True, blank=True, help_text="Код родительского региона")

    class Meta:
        db_table = "system_area"
        verbose_name = 'Таблица регионов'
        verbose_name_plural = verbose_name
        ordering = ('code',)

    def __str__(self):
        return f"{self.name}"


class ApiWhiteList(CoreModel):
    url = models.CharField(max_length=200, help_text="Адрес url", verbose_name="url")
    METHOD_CHOICES = (
        (0, "GET"),
        (1, "POST"),
        (2, "PUT"),
        (3, "DELETE"),
    )
    method = models.IntegerField(default=0, verbose_name="Метод запроса интерфейса", null=True, blank=True,
                                 help_text="Метод запроса интерфейса")
    enable_datasource = models.BooleanField(default=True, verbose_name="Активировать права доступа к данным", help_text="Активировать права доступа к данным",
                                            blank=True)

    class Meta:
        db_table = "system_api_white_list"
        verbose_name = 'Белый список интерфейсов'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)


class SystemConfig(CoreModel):
    parent = models.ForeignKey(to='self', verbose_name='Родительский элемент', on_delete=models.CASCADE,
                               db_constraint=False, null=True, blank=True, help_text="Родительский элемент")
    title = models.CharField(max_length=50, verbose_name="Заголовок", help_text="Заголовок")
    key = models.CharField(max_length=20, verbose_name="Ключ", help_text="Ключ")
    value = models.JSONField(max_length=100, verbose_name="Значение", help_text="Значение", null=True, blank=True)
    status = models.BooleanField(default=False, verbose_name="Состояние активации", help_text="Состояние активации")
    data_options = models.JSONField(verbose_name="Параметры данных", help_text="Параметры данных", null=True, blank=True)
    FORM_ITEM_TYPE_LIST = (
        (0, 'text'),
        (1, 'textarea'),
        (2, 'number'),
        (3, 'select'),
        (4, 'radio'),
        (5, 'checkbox'),
        (6, 'date'),
        (7, 'datetime'),
        (8, 'time'),
        (9, 'imgs'),
        (10, 'files'),
        (11, 'array'),
        (12, 'foreignkey'),
        (13, 'manytomany'),
    )
    form_item_type = models.IntegerField(choices=FORM_ITEM_TYPE_LIST, verbose_name="Тип формы", help_text="Тип формы",
                                         default=0,
                                         blank=True)
    rule = models.JSONField(null=True, blank=True, verbose_name="Правила проверки", help_text="Правила проверки")
    placeholder = models.CharField(max_length=50, null=True, blank=True, verbose_name="Подсказка", help_text="Подсказка")
    setting = models.JSONField(null=True, blank=True, verbose_name="Настройка", help_text="Настройка")

    class Meta:
        db_table = "system_config"
        verbose_name = 'Таблица системной конфигурации'
        verbose_name_plural = verbose_name
        ordering = ('sort',)

    def __str__(self):
        return f"{self.title}"


class LoginLog(CoreModel):
    LOGIN_TYPE_CHOICES = (
        (1, 'Обычный вход'),
    )
    username = models.CharField(max_length=32, verbose_name="Имя пользователя при входе", null=True, blank=True, help_text="Имя пользователя при входе")
    ip = models.CharField(max_length=32, verbose_name="IP при входе", null=True, blank=True, help_text="IP при входе")
    agent = models.TextField(verbose_name="Информация об агенте", null=True, blank=True, help_text="Информация об агенте")
    browser = models.CharField(max_length=200, verbose_name="Название браузера", null=True, blank=True, help_text="Название браузера")
    os = models.CharField(max_length=200, verbose_name="Операционная система", null=True, blank=True, help_text="Операционная система")
    continent = models.CharField(max_length=50, verbose_name="Континент", null=True, blank=True, help_text="Континент")
    country = models.CharField(max_length=50, verbose_name="Страна", null=True, blank=True, help_text="Страна")
    province = models.CharField(max_length=50, verbose_name="Область", null=True, blank=True, help_text="Область")
    city = models.CharField(max_length=50, verbose_name="Город", null=True, blank=True, help_text="Город")
    district = models.CharField(max_length=50, verbose_name="Район", null=True, blank=True, help_text="Район")
    isp = models.CharField(max_length=50, verbose_name="Оператор связи", null=True, blank=True, help_text="Оператор связи")
    area_code = models.CharField(max_length=50, verbose_name="Код региона", null=True, blank=True, help_text="Код региона")
    country_english = models.CharField(max_length=50, verbose_name="Полное название на английском", null=True, blank=True,
                                       help_text="Полное название на английском")
    country_code = models.CharField(max_length=50, verbose_name="Сокращенное название", null=True, blank=True, help_text="Сокращенное название")
    longitude = models.CharField(max_length=50, verbose_name="Долгота", null=True, blank=True, help_text="Долгота")
    latitude = models.CharField(max_length=50, verbose_name="Широта", null=True, blank=True, help_text="Широта")
    login_type = models.IntegerField(default=1, choices=LOGIN_TYPE_CHOICES, verbose_name="Тип входа",
                                     help_text="Тип входа")

    class Meta:
        db_table = 'system_login_log'
        verbose_name = 'Журнал входа'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)


class GeneratorTemplate(CoreModel):
    name = models.CharField(null=False, max_length=64, verbose_name="Название шаблона", help_text="Название шаблона")
    code = models.CharField(max_length=32, verbose_name="Код шаблона", help_text="Код шаблона")
    form_info = models.TextField(verbose_name="Информация о форме", help_text="Информация о форме")
    table_info = models.TextField(verbose_name="Информация о таблице", help_text="Информация о таблице")
    has_menu = models.BooleanField(default=False, verbose_name="Было ли сгенерировано меню", help_text="Было ли сгенерировано меню")

    class Meta:
        db_table = "system_generator_template"
        verbose_name = 'Шаблон генератора кода'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)